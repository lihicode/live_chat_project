# first of all import the socket library
import socket
import threading

"""
function: extracts the indexes of the client list and converts them to string
input: client list
"""
# func that returns a list of ip and port connections
def addr_extractor(client_list):
    names_list = []
    for part in client_list:
        names_list.append(part[1])
    return_string = ''.join(str(names_list.index(x)) + ', ' for x in names_list)
    return return_string

"""
function: lets the client choosse a friend to send messages to
input: client socket
"""
#func that lets the client choose a client to talk to
def choose_friend(client):
    client.send((" choose a friend from the list: \n" + addr_extractor(client_list)).encode())
    chosen_index = int(client.recv(1024).decode())
    return client_list[chosen_index][0]

"""
function: updates the list of clients every time a client connects or disconnects
"""
def client_updater():
    updated_client_list = addr_extractor(client_list)
    print(updated_client_list)
    for client in client_list:
        client[0].send(("updated client list: " + updated_client_list).encode())

"""
function: sends and receives messages from the client
input: client socket + client ip and port
"""
def user_handler(client, addr):
    #encoding to send byte type.
    client.send('Thank you for connecting'.encode())
    try:
        while True:
            chosen_client = choose_friend(client)
            client.send("Friend selected. You can start chatting".encode())
            while True:
                msg = (client.recv(1024).decode())
                if msg == "/exit":
                    client.send("You left the chat. Choose another friend.".encode())
                    client.send(("Choose a friend from the list: \n" + addr_extractor(client_list)).encode())
                    break
                if msg == "/quit":
                    client.send("Goodbye!".encode())
                    chosen_client.send("Your friend disconnected. Type /exit to choose another friend.".encode())
                    client_list.remove((client, addr))
                    client_updater()
                    client.close()
                    return
                msg = f'Message from friend: {msg}'
                print(msg)
                chosen_client.send(msg.encode())
    except:
        client_list.remove((client, addr))
        print("this is it:", client_list)
        client_updater()

#socket creation, binding to the chosen port and listening
server_socket = socket.socket()
print("Socket successfully created")
port = 12345
server_socket.bind(('', port))
print("socket binded to %s" % port)
server_socket.listen(5)
print("socket is listening")

client_list = []
while True:
    # connection with client
    client_socket, addr = server_socket.accept()
    print('Got connection from', addr)
    # adding to the client list the ip and port of the new connection
    client_list.append((client_socket, addr))
    client_updater()
    threading.Thread(target=user_handler, args=(client_socket, addr)).start()