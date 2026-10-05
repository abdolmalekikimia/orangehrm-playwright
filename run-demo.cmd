@echo off
setlocal
cd /d "%~dp0"
if exist .venv\Scripts\python.exe goto install
call :try_python py -3
if exist .venv\Scripts\python.exe goto install
call :try_python python
if exist .venv\Scripts\python.exe goto install
if defined ORANGEHRM_PYTHON call :try_python "%ORANGEHRM_PYTHON%"
if exist .venv\Scripts\python.exe goto install
call :try_python "%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
if exist .venv\Scripts\python.exe goto install
for /d %%P in ("%LOCALAPPDATA%\Programs\Python\Python*") do if not exist .venv\Scripts\python.exe call :try_python "%%P\python.exe"
if not exist .venv\Scripts\python.exe goto failed
:install
.venv\Scripts\python.exe -m pip install -r requirements.txt
if errorlevel 1 goto failed
if /i "%~1"=="--setup-only" exit /b 0
.venv\Scripts\python.exe -m pytest --headed --browser-channel chrome --slowmo 500 %*
set result=%errorlevel%
if exist reports\index.html start "" reports\index.html
pause
exit /b %result%
:try_python
"%~1" %2 -c "import sys; sys.exit(0 if sys.version_info >= (3,11) else 1)" >nul 2>&1
if errorlevel 1 exit /b 1
echo Creating virtual environment with %~1
"%~1" %2 -m venv .venv
exit /b %errorlevel%
:failed
echo Setup failed. Python 3.11+ and Google Chrome are required.
echo If Python is installed elsewhere, set ORANGEHRM_PYTHON to its python.exe path and retry.
pause
exit /b 1
