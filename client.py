#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
print host
port = 12345                # Reserve a port for your service.

myVar = s.connect((host, port))
print s.recv(1024)
s.close    
