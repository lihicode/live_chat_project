# first of all import the socket library
import socket
import threading

def user_handler(client):
    while True:
        # send a message to the client. encoding to send byte type.
        client.send('Thank you for connecting'.encode())
        print(client.recv(1024).decode())


# next create a socket object
s = socket.socket()
print("Socket successfully created")

# reserve a port on your computer
port = 12345

s.bind(('', port))
print("socket binded to %s" % (port))

# put the socket into listening mode
s.listen(5)
print("socket is listening")

while True:
    # Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)
    threading.Thread(target = user_handler(c)).start()
    c.close()
