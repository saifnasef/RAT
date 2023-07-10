import socket, sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ser = ("192.168.1.102", 8087)
s.connect(ser)
path = sys.argv[1]

def download():
    f = open(path, 'a')
    data = s.recv(10000)
    f.write(data.decode())
    f.close()
    s.close()

def upload():
    name = path.rsplit("\\", 1)[1]
    s.send(name.encode())
    f = open(name, 'r')
    data = f.read()
    f.close()
    s.send(data.encode())
    s.close()

if sys.argv[2] == "upload":
    upload()
elif sys.argv[2] == "download":
    download()
