#import requests.packages.urllib3.util.ssl_
#print(requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS)
#requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'RSA+AES'
##>>> requests.get('https://kennethreitz.com', cert=('/path/client.cert', '/path/client.key'))
##<Response [200]>

#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)
s.close    
