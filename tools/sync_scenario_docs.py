"""Synchronize catalog, readable plan and optional Wiki from collected markers.

Run: python tools/sync_scenario_docs.py --map reports/scenario-map.json
Optionally add --wiki-dir PATH to generate the Wiki pages before publishing.
This updates implementation metadata only; it never turns a run into Pass evidence.
"""
import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--map", required=True, type=Path)
    parser.add_argument("--wiki-dir", type=Path)
    parser.add_argument("--updated-on", default="2026-10-06")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    docs = root / "docs/test-plan"
    catalog = docs / "scenario-catalog.json"
    data = json.loads(catalog.read_text(encoding="utf-8"))
    mapping = json.loads(args.map.read_text(encoding="utf-8"))
    if not mapping.get("complete_collection"):
        raise SystemExit("Refusing to synchronize from a subset. Collect the complete default tests directory without -k/-m or selected files.")
    variations = mapping["results"]
    assert all(v["scenario_id"] in {c["id"] for c in data["cases"]} for v in variations)
    for case in data["cases"]:
        mapped = [v for v in variations if v["scenario_id"] == case["id"]]
        case["status"] = "automated" if any(v["coverage"] == "full" for v in mapped) else "partial" if mapped else "planned"
        case["test"] = mapped[0]["nodeid"] if mapped else ""
        case["test_references"] = [v["nodeid"] for v in mapped]
        case["automation_variations"] = [{k:v[k] for k in ("nodeid", "coverage", "variation")} for v in mapped]
        if case["id"] in {"AUTH-008", "AUTH-011", "AUTH-012", "MAINT-001"}:
            case["env"] = "R"
            case["pre"] = "Reachable public demo; valid published Admin credentials where authentication is required. No business-data mutation."
    counts = Counter(c["status"] for c in data["cases"])
    total = len(data["cases"])
    summary = f"{total} designed scenarios: {counts['automated']} automated, {counts['partial']} partially automated and {counts['planned']} planned; {len(variations)} executable test variations."
    data["version"] = "1.1-en"
    data["automation_updated_on"] = args.updated_on
    data["notes"][0] = "This is a scenario plan and automation backlog, not evidence that every feature or combination has been tested. " + summary + " Implementation status is separate from execution outcome."
    data["notes"] = [n.replace("two existing test files", "current test source") for n in data["notes"]]
    catalog.write_text(json.dumps(data, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    with (docs/"scenario-catalog.csv").open("w", encoding="utf-8-sig", newline="") as stream:
        writer=csv.DictWriter(stream,fieldnames=list(data["cases"][0]));writer.writeheader()
        for c in data["cases"]:
            writer.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in c.items()})
    def area_table(wiki=False):
        lines=["| Area | Scenarios | Automated | Partial | Planned |","|---|---:|---:|---:|---:|"]
        for s in data["sections"]:
            cc=Counter(c["status"] for c in data["cases"] if c["section"]==s["prefix"])
            dest=wiki_url+"/"+wiki_names[s['prefix']] if wiki else s['file']
            lines.append(f"| [{s['title']}]({dest}) | {sum(cc.values())} | {cc['automated']} | {cc['partial']} | {cc['planned']} |")
        lines.append(f"| **Total** | **{total}** | **{counts['automated']}** | **{counts['partial']}** | **{counts['planned']}** |")
        return "\n".join(lines)
    repo_url="https://github.com/abdolmalekikimia/orangehrm-playwright"
    wiki_url=repo_url+"/wiki"
    wiki_names={'AUTH':'Authentication','COMMON':'Shared-Controls','ADMIN':'Admin','PIM':'PIM','PROFILE':'My-Info','LEAVE':'Leave','TIME':'Time','RECRUIT':'Recruitment','PERF':'Performance','DASH':'Dashboard','DIR':'Directory','MAINT':'Maintenance','CLAIM':'Claim','BUZZ':'Buzz','RBAC':'Authorization-and-Integration'}
    labels={"automated":"Automated for the specified scenario scope","partial":"Partially automated; remaining variations are planned","planned":"Planned; no implemented test"}
    for section in data["sections"]:
        cases=[c for c in data["cases"] if c["section"]==section["prefix"]]
        cc=Counter(c['status'] for c in cases)
        lines=[f"# {section['title']}","",f"**{len(cases)} scenarios | {cc['automated']} automated | {cc['partial']} partial | {cc['planned']} planned**","",
               "[Plan overview](README.md) | [CSV catalog](scenario-catalog.csv) | [JSON catalog](scenario-catalog.json)","","## Scope","",section['scope'],"","## Default prerequisites","",section['pre'],"",
               "Shared controls and [evidence rules](README.md) also apply. R = read-only public demo; I = isolated instance; D = disposable instance. Partial implementations run only their documented public-demo variation, not the complete I/D workflow.","","## Scenario index","","| ID | Scenario | Design environment | Implementation status |","|---|---|---|---|"]
        for c in cases:lines.append(f"| [{c['id']}](#{c['id'].lower()}) | {c['title']} | {c['env']} | {c['status'].title()} |")
        lines += ["","## Scenarios",""]
        for c in cases:
            lines += [f"### {c['id']}","",f"**{c['title']}**","",f"**Priority:** {c['priority']} · **Design environment:** {c['env']} · **Role:** {c['role']} · **Automation:** {labels[c['status']]}","",
                      f"**Prerequisites:** {c['pre']}","",f"**Steps / test data:** {c['steps']}","",f"**Expected outcome:** {c['expected']}",""]
            if c['automation_variations']:
                lines += [f"<details><summary>Implemented variations ({len(c['automation_variations'])})</summary>","","| Source test | Scope | Implemented variation |","|---|---|---|"]
                for v in c['automation_variations']:
                    file=v['nodeid'].split('::')[0]
                    lines.append(f"| [`{v['nodeid']}`]({repo_url}/blob/main/{file}) | {v['coverage']} | {v['variation'] or 'Specified scenario scope'} |")
                lines += ["","</details>","","Implementation metadata is not a fresh passing execution result.",""]
        lines += ["[Back to scenario index](#scenario-index) | [Back to plan overview](README.md)",""]
        (docs/section['file']).write_text("\n".join(lines),encoding="utf-8")
    overview=(docs/'README.md').read_text(encoding='utf-8')
    overview=re.sub(r'\*\*(?:323 scenarios across all 12 main modules\.|323 designed scenarios:).*?\*\*',"**"+summary+"**",overview,count=1)
    overview=re.sub(r'> This is the planned test scope.*',"> Implementation scope and execution outcome are separate. The public-demo suite covers the mapped read-only variations; the remaining workflows require isolated fixtures and approved rules.",overview,count=1)
    overview=re.sub(r'(## Browse by area\n\n).*?(\n\nEach area)',lambda m:m.group(1)+area_table()+m.group(2),overview,flags=re.S)
    overview=re.sub(r'1\. This is a scenario plan.*',"1. "+data['notes'][0],overview,count=1)
    overview=overview.replace('1. Preserve the existing 10 R cases; extend read-only navigation and nonmutating search coverage for the public demo.','1. Run the mapped public-demo cases, inspect per-scenario evidence and distinguish full from partial scope.')
    (docs/'README.md').write_text(overview,encoding='utf-8')
    auto=["# Implementation Coverage","",summary,"","This table is generated from collected `scenario` markers. Full means the specified scenario scope has an implementation; partial means only the named variations are implemented. Neither means the latest run passed.","",area_table(),"","## Implemented mappings","","| ID | Status | Test variations |","|---|---|---:|"]
    for c in data['cases']:
        if c['status']!='planned':auto.append(f"| [{c['id']}]({next(s['file'] for s in data['sections'] if s['prefix']==c['section'])}#{c['id'].lower()}) | {c['status']} | {len(c['automation_variations'])} |")
    auto += ["","## Reports","","- `reports/index.html`: test results with scenario ID, scope and variation.","- `reports/junit.xml`: machine-readable results and scenario properties.","- `reports/scenario-results.json`: actual outcomes, fixture errors, selected variations and unmapped scenarios.","- A subset run has only its selected cases; unselected scenarios are not failures or passes.","","## Regenerate implementation metadata","","```powershell",".\\.venv\\Scripts\\python.exe -m pytest --collect-only -q -o addopts='' --scenario-map reports/scenario-map.json",".\\.venv\\Scripts\\python.exe tools/sync_scenario_docs.py --map reports/scenario-map.json","```","","Add `--wiki-dir PATH` to render a Wiki checkout before publishing. No live tests or mutations run during documentation generation.",""]
    (docs/'automation-coverage.md').write_text('\n'.join(auto),encoding='utf-8')
    main_readme=(root/'README.md').read_text(encoding='utf-8')
    metrics=f"| Measure | Current scope |\n|---|---|\n| Test design | {total} scenarios across all 12 main modules |\n| Automated | {counts['automated']} scenarios with full specified scope |\n| Partial | {counts['partial']} scenarios with limited implemented variations |\n| Planned | {counts['planned']} scenarios without automation |\n| Executable checks | {len(variations)} mapped test variations |"
    main_readme=re.sub(r'\| Measure \| Current scope \|.*?(?=\n\n)',metrics,main_readme,flags=re.S)
    main_readme=re.sub(r'The current suite covers.*?\n',"The suite maps every test to a scenario ID. It covers login/session checks, all 12 module landing pages, 53 submenu destinations, protected entry routes, sidebar search, two text filters/reset and Maintenance cancellation. Broad navigation/filter/authorization cases are explicitly partial. No business records or configuration are changed.\n",main_readme,count=1)
    scope_note = ' Reports label full/partial scope and actual outcomes separately.'
    main_readme=main_readme.replace(scope_note, '')
    main_readme=main_readme.replace('not the entire 323-scenario plan.','not the entire 323-scenario plan.' + scope_note)
    main_readme=main_readme.replace('failures retain screenshots/traces in `reports/artifacts`.','failures retain screenshots/traces in `reports/artifacts`; scenario outcomes are in `reports/scenario-results.json` and JUnit in `reports/junit.xml`.')
    (root/'README.md').write_text(main_readme,encoding='utf-8')
    if args.wiki_dir:
        w=args.wiki_dir;w.mkdir(parents=True,exist_ok=True)
        replacements={s['file']:wiki_url+'/'+wiki_names[s['prefix']] for s in data['sections']}
        replacements.update({'README.md':wiki_url+'/Home','scenario-catalog.csv':repo_url+'/blob/main/docs/test-plan/scenario-catalog.csv','scenario-catalog.json':repo_url+'/blob/main/docs/test-plan/scenario-catalog.json'})
        def wiki_links(text):
            for old,new in replacements.items():
                text=re.sub(r'\]\(' + re.escape(old) + r'(?=[#)])', lambda match: '](' + new, text)
            return text
        for s in data['sections']:(w/(wiki_names[s['prefix']]+'.md')).write_text(wiki_links((docs/s['file']).read_text(encoding='utf-8')),encoding='utf-8')
        (w/'Automation-Coverage.md').write_text(wiki_links('\n'.join(auto)),encoding='utf-8')
        for name in ('Home','Test-Scenario-Index','Detailed-Test-Cases'):
            path=w/(name+'.md')
            if not path.exists():continue
            text=path.read_text(encoding='utf-8')
            text=re.sub(r'\*\*(?:323 scenarios across 12 main modules:|323 designed scenarios:).*?\*\*',"**"+summary+"**",text)
            text=re.sub(r'\| Area \| Scenarios \| Automated \| (?:Partial \| )?Planned \|.*?\| \*\*Total\*\* .*?\n',area_table(wiki=True)+'\n',text,flags=re.S)
            text=text.replace('The runnable public-demo suite currently covers login, validation, session protection and basic navigation.','The runnable suite maps read-only login, session, navigation and search variations to the catalog; partial scope is labeled explicitly.')
            text=text.replace('The 10 implemented cases and their source references.','Implemented full/partial scope, executable variations and source references.')
            if name=='Detailed-Test-Cases' and '**Partially automated:**' not in text:
                text=text.replace('- **Planned:**','- **Partially automated:** only the listed variations have code; the remaining scenario scope is not implemented.\n- **Planned:**')
            path.write_text(text,encoding='utf-8')
        footer=w/'_Footer.md'
        if footer.exists():footer.write_text(re.sub(r'323 designed scenarios.*',summary+' Inventory: 2026-10-05.',footer.read_text(encoding='utf-8')),encoding='utf-8')
        strategy=w/'Test-Strategy.md'
        if strategy.exists():
            text=strategy.read_text(encoding='utf-8')
            text=re.sub(r'1\. This is a scenario plan.*',"1. "+data['notes'][0],text,count=1)
            text=text.replace('1. Preserve the existing 10 R cases; extend read-only navigation and nonmutating search coverage for the public demo.','1. Run mapped public-demo variations and assess per-scenario evidence; separate full and partial scope.')
            strategy.write_text(text,encoding='utf-8')
        execution=w/'Test-Execution.md'
        if execution.exists():
            text=re.sub(r'The default suite contains[^\n]*',f'The default suite contains {len(variations)} executable read-only variations mapped to {counts["automated"]} full and {counts["partial"]} partial scenarios.',execution.read_text(encoding='utf-8'))
            report_note = 'Scenario results: `reports/scenario-results.json`; JUnit: `reports/junit.xml`. HTML rows include the scenario ID and implemented scope.'
            text = text.replace(report_note + '\n', '').rstrip() + '\n\n' + report_note + '\n'
            execution.write_text(text,encoding='utf-8')
    print(summary)


if __name__ == '__main__':
    main()
