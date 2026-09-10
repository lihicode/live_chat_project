# Import socket module
import socket
import threading

def wait_for_message():
    while True:
        print(client_socket.recv(1024).decode())

def send_message():
    while True:
        client_message = input("Enter a message to the server: \n")
        client_socket.send(client_message.encode())

# Create a socket object
client_socket = socket.socket()

# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
client_socket.connect(('127.0.0.1', port))

# receive data from the server and decoding to get the string.
print (client_socket.recv(1024).decode())

threading.Thread(target=wait_for_message).start()
threading.Thread(target=send_message).start()

# close the connection
#client_socket.close()