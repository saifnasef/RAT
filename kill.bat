TASKKILL /F /IM rev.exe
powershell del C:\Users\%username%\AppData\Local\Temp\MicroWindows -Recurse -Force /Q
del "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\startup.bat" -Recurse -Force /Q
reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 1 /f