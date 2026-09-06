# Import socket module
import socket

# Create a socket object
s2 = socket.socket()

# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
s2.connect(('127.0.0.1', port))
mishtane = "lior"
while(mishtane != "exit"):
    # receive data from the server and decoding to get the string.
    print (s2.recv(1024).decode())
    mishtane = input("i love life")
    s2.send(mishtane.encode())

# close the connection
s.close()