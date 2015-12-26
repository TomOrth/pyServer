import socket

host, port = '', 8888

listenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listenSocket.bind((host,port))
listenSocket.listen(1)

print 'Serving HTTP on port %s...' % port
while True:
    clientConn, clientAddr = listenSocket.accept()
    request = clientConn.recv(1024)
    print request
    
    httpResponse = """\
HTTP/1.1 200 OK

Hello, World!
"""
    clientConn.sendall(httpResponse)
    clientConn.close()
