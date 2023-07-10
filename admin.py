import socket,time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.9", 8080))
s.send(b"auth")
time.sleep(0.5)
s.send(b"urmom")
time.sleep(2)
d = s.recv(1024)
print(d.decode())
op = input()
if op == "1" or op == "command":
    s.send(b"1")
    username = input("Username: ")
    s.send(username.encode())
    while True:
        command = input("Enter command: ")
        s.send(command.encode())
        res = s.recv(1024)
        print(res.decode())