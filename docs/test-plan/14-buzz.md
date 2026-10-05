# Buzz social feed

**11 scenarios | 0 automated | 11 planned**

[Plan overview](README.md) | [CSV catalog](scenario-catalog.csv) | [JSON catalog](scenario-catalog.json)

## Scope

Post; Photos; Video; Most Recent/Liked/Commented; likes/comments/shares; authorized editing/deletion.

## Default prerequisites

Synthetic posts/media in an isolated instance; do not publish content to the shared public demo.

Shared controls and evidence rules in [COMMON](02-common.md) and the [overview](README.md) also apply. Environment codes: R = read-only demo, I = isolated instance, D = disposable instance.

## Scenario index

| ID | Scenario | Environment | Automation status |
|---|---|---|---|
| [BUZZ-001](#buzz-001) | Post: valid and empty text | I | Planned |
| [BUZZ-002](#buzz-002) | Post: edit and delete permissions | I | Planned |
| [BUZZ-003](#buzz-003) | Share Photos | I | Planned |
| [BUZZ-004](#buzz-004) | Share Video | I | Planned |
| [BUZZ-005](#buzz-005) | Like and Unlike | I | Planned |
| [BUZZ-006](#buzz-006) | Comments | I | Planned |
| [BUZZ-007](#buzz-007) | Share Post | I | Planned |
| [BUZZ-008](#buzz-008) | Sorting and feed pagination | I | Planned |
| [BUZZ-009](#buzz-009) | Read More and media dialogs | I | Planned |
| [BUZZ-010](#buzz-010) | Birthday and anniversary widgets | I | Planned |
| [BUZZ-011](#buzz-011) | Feed refresh and publishing failures | I | Planned |

## Scenarios

### BUZZ-001

**Post: valid and empty text**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Synthetic posts/media in an isolated instance; do not publish content to the shared public demo.

**Steps / test data:** Post plain/multiline/Persian/long text; test empty and whitespace-only content.

**Expected outcome:** Valid content displays intact within actual limits; empty-input policy applies; one submission creates one post.

### BUZZ-002

**Post: edit and delete permissions**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Synthetic posts/media in an isolated instance; do not publish content to the shared public demo.

**Steps / test data:** Edit/save/cancel your own fixture; cancel/confirm deletion; inspect another account's post as ESS.

**Expected outcome:** Only the owner/authorized role can change it; cancellation preserves content; unrelated posts are unaffected.

### BUZZ-003

**Share Photos**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Synthetic posts/media in an isolated instance; do not publish content to the shared public demo.

**Steps / test data:** Test one/multiple valid photos, oversized/disallowed files, removing previews and Cancel.

**Expected outcome:** Previews are correct; only accepted files are published; cancellation leaves no post/file behind.

### BUZZ-004

**Share Video**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Synthetic posts/media in an isolated instance; do not publish content to the shared public demo.

**Steps / test data:** Test supported, malformed and unsupported-provider URLs; Cancel.

**Expected outcome:** Embedding follows the version's capabilities; unsafe/invalid URLs are rejected without executing unsafe content.

### BUZZ-005

**Like and Unlike**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Synthetic posts/media in an isolated instance; do not publish content to the shared public demo.

**Steps / test data:** Like/unlike a fixture using a test account; click twice quickly; reload and inspect with a second account.

**Expected outcome:** One reaction per account; counters remain correct; removing a reaction affects only that account's contribution.

### BUZZ-006

**Comments**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Synthetic posts/media in an isolated instance; do not publish content to the shared public demo.

**Steps / test data:** Add valid/empty/long comments; edit/delete own comments if supported; inspect from another account.

**Expected outcome:** Text/counts are correct; permission rules apply; empty or executable content is handled safely.

### BUZZ-007

**Share Post**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Synthetic posts/media in an isolated instance; do not publish content to the shared public demo.

**Steps / test data:** Share a fixture with/without text; cancel and repeat.

**Expected outcome:** Original-post association and counters follow the version; cancellation creates no share; author/original are not misidentified.

### BUZZ-008

**Sorting and feed pagination**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Synthetic posts/media in an isolated instance; do not publish content to the shared public demo.

**Steps / test data:** Use known posts with differing dates/likes/comments; select all three sorts; scroll/load more.

**Expected outcome:** Ordering follows the chosen criterion and tie policy; posts are not unintentionally repeated or missing.

### BUZZ-009

**Read More and media dialogs**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Synthetic posts/media in an isolated instance; do not publish content to the shared public demo.

**Steps / test data:** Expand/collapse long text; view photos/videos and close the dialog.

**Expected outcome:** Full content is accessible without layout damage; focus returns; broken media has a clear error state.

### BUZZ-010

**Birthday and anniversary widgets**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Synthetic posts/media in an isolated instance; do not publish content to the shared public demo.

**Steps / test data:** If present, use synthetic employees with boundary dates and a known timezone.

**Expected outcome:** Correct people/dates appear without excess disclosure; absent widgets are N/A.

### BUZZ-011

**Feed refresh and publishing failures**

**Priority:** P1 · **Environment:** I · **Role:** Admin / ESS · **Automation:** Planned; not implemented or executed as part of this plan

**Prerequisites:** Synthetic posts/media in an isolated instance; do not publish content to the shared public demo.

**Steps / test data:** Create a post from a second test account; refresh; inject a controlled publish failure.

**Expected outcome:** Fresh content appears; failed publishing is not reported as success; retry does not create duplicate posts.

[Back to scenario index](#scenario-index) | [Back to plan overview](README.md)
