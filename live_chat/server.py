# first of all import the socket library
import socket
import threading

"""
function:
input:
output:
"""
# func that returns a list of ip and port connections
def addr_extractor(client_list):
    names_list = []
    for part in client_list:
        names_list.append(part[1])
    return_string = ''.join(str(names_list.index(x)) + ', ' for x in names_list)
    return return_string

"""
function:
input:
output:
"""
#func that lets the client choose a client to talk to
def choose_friend(client):
    client.send((" choose a friend from the list or \n" + addr_extractor(client_list)).encode())
    chosen_index = int(client.recv(1024).decode())
    return client_list[chosen_index][0]

"""
function:
input:
output:
"""
def client_updater():
    updated_client_list = addr_extractor(client_list)
    print(updated_client_list)
    for client in client_list:
        client[0].send(("updated client list: " + updated_client_list).encode())

"""
function:
input:
output:
"""
# func that sends and receives messages from the client
def user_handler(client, addr):
    # send a message to the client. encoding to send byte type.
    client.send('Thank you for connecting'.encode())
    client.send(''.encode())
    try:
        while True:
            chosen_client = choose_friend(client)
            client.send("Friend selected. You can start chatting".encode())
            while True:
                #print("this is the client list for the server's eyes only:", addr_extractor(client_list))
                msg = (client.recv(1024).decode())
                if msg == "/exit":
                    client.send("You left the chat. Choose another friend.".encode())
                    client.send(("choose a friend from the list: \n" + addr_extractor(client_list)).encode())
                    break
                msg = f'message from friend: {msg}'
                print(msg)
                chosen_client.send(msg.encode())
    except:
        client_list.remove((client, addr))
        print("this is it:", client_list)
        client_updater()


# next create a socket object
server_socket = socket.socket()
print("Socket successfully created")
# reserve a port on your computer
port = 12345
#binds the socket
server_socket.bind(('', port))
print("socket binded to %s" % port)
# put the socket into listening mode
server_socket.listen(5)
print("socket is listening")

client_list = []

while True:
    # Establish connection with client.
    client_socket, addr = server_socket.accept()
    print('Got connection from', addr)
    # adding to the client list the ip and port of the new connection
    client_list.append((client_socket, addr))
    client_updater()
    threading.Thread(target=user_handler, args=(client_socket, addr)).start()