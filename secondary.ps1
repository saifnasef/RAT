
mkdir C:/temp
Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.7.0/python-3.7.0.exe" -OutFile "c:/temp/python-3.7.0.exe"
c:/temp/python-3.7.0.exe /quiet InstallAllUsers=0 PrependPath=1 Include_test=0
