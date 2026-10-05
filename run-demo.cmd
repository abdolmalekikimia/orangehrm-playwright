@echo off
cd /d "%~dp0"
if not exist .venv\Scripts\python.exe (
  py -3 -m venv .venv
  if errorlevel 1 goto failed
)
.venv\Scripts\python.exe -m pip install -r requirements.txt
if errorlevel 1 goto failed
.venv\Scripts\python.exe -m pytest --headed --browser-channel chrome --slowmo 500 %*
set result=%errorlevel%
if exist reports\index.html start "" reports\index.html
pause
exit /b %result%
:failed
echo Setup failed. Install Python 3.11+ with the Python launcher and Google Chrome, then check your internet connection.
pause
exit /b 1
