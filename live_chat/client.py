# Import socket module
import socket
import threading
import sys

"""
function: client waits for a message from the server
"""
def wait_for_message():
    while True:
        server_message = client_socket.recv(1024).decode()
        # print and enter a line
        sys.stdout.write(f"\r\033[K{server_message}\n Send a message: ")
        #free the buffer
        sys.stdout.flush()
"""
function: sends a message to the server
"""
def send_message():
    while True:
        client_message = input("Send a message: \n")
        client_socket.send(client_message.encode())
        if client_message == "/quit":
            client_socket.close()

client_socket = socket.socket()
port = 12345
client_socket.connect(('127.0.0.1', port))

# receive data from the server and decoding to get the string.
print (client_socket.recv(1024).decode())

threading.Thread(target=wait_for_message).start()
threading.Thread(target=send_message).start()