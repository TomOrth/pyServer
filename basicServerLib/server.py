import socket

class Server(object):
    def __init__(self, msg):
        self.msg = msg
    def listen(self, host='', port=8888):
       self.host = host
       self.port = port 
       listenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
       listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
       listenSocket.bind((self.host,self.port))
       listenSocket.listen(1)
        
       print 'Server is listening at %s...' % self.port
       while True:
           clientConn, clientAddr = listenSocket.accept()
           req = clientConn.recv(1024)
           httpResponse = """\
HTTP/1.1 200 OK

""" + self.msg 
           clientConn.sendall(httpResponse)
           clientConn.close()
        

