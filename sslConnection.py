import ssl
import socket

if ssl.HAS_SNI:
    print "SNI is available"
print(ssl.OPENSSL_VERSION)

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.load_cert_chain('cacrt.pem', 'cakey.pem', 'password')
context.set_ciphers('RC4-SHA')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


sock = context.wrap_socket(sock, server_hostname='virtServer')
#instead sock.write('...') and sock.recv() to make the request



sock.connect(('ip.to.the.server', 443))

http_client = tornado.httpclient.HTTPClient()
http_client.fetch('https://ip.to.the.server/some_url', method='GET',  ssl_options=context)
