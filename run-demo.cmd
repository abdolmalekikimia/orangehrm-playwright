@echo off
cd /d "%~dp0"
if not exist .venv\Scripts\python.exe (
  py -3 -m venv .venv
  if errorlevel 1 goto failed
)
.venv\Scripts\python.exe -m pip install -r requirements.txt
if errorlevel 1 goto failed
.venv\Scripts\python.exe -m playwright install chromium
if errorlevel 1 (
  echo Chromium download failed. Trying installed Google Chrome instead.
  .venv\Scripts\python.exe -m pytest --browser-channel chrome %*
) else (
  .venv\Scripts\python.exe -m pytest %*
)
set result=%errorlevel%
if exist reports\index.html start "" reports\index.html
pause
exit /b %result%
:failed
echo Setup failed. Install Python 3.11+ with the Python launcher and check your internet connection.
pause
exit /b 1
