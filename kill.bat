TASKKILL /F /IM rev.exe
powershell Remove-Item C:\Users\%username%\AppData\Local\Temp\MicroWindows -Recurse 
del "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\startup.bat" -Recurse -Force /Q
reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 1 /f
del "%~f0"