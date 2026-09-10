# Import socket module
import socket
import threading
import sys

"""
function:
input:
output:
"""
def wait_for_message():
    while True:
        server_message = client_socket.recv(1024).decode()
        #like print and enter a line
        sys.stdout.write(f"\r\033[K{server_message}\n Enter a message to the server: ")
        #like free the buffer
        sys.stdout.flush()


"""
function:
input:
output:
"""
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
#client_socket.send("/new".encode())
print(client_socket)

# receive data from the server and decoding to get the string.
print (client_socket.recv(1024).decode())

threading.Thread(target=wait_for_message).start()
threading.Thread(target=send_message).start()