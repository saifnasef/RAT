import os,sys

cd = os.path.abspath(sys.argv[0])
cd = cd.rsplit("\\", 1)[0]
cd += "\\Logs\\keylog.txt"
data = ""
print(cd)
f = open(cd, 'r')
data += f.read()
print(data)