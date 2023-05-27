# Specify the program's name and path
$programName = "MyProgram"
$programPath = "C:\Path\To\Program.exe"

# Set the registry path for current user startup
$registryPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"

# Add the program to startup in the registry
Set-ItemProperty -Path $registryPath -Name $programName -Value $programPath


# Specify the program's name and path
$programName = "MyProgram"
$programPath = "C:\Path\To\Program.exe"

# Get the startup folder path
$startupFolderPath = [Environment]::GetFolderPath("Startup")

# Create a shortcut to the program in the startup folder
$shortcutPath = Join-Path -Path $startupFolderPath -ChildPath "$programName.lnk"
$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut($shortcutPath)
$Shortcut.TargetPath = $programPath
$Shortcut.Save()