import socket
class Server(object):
    def __init__(self, type):
        self.type = type
    def listen(self, host='', port=8888, response="hello"):
       self.host = host
       self.port = port 
       self.response = response
       listenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
       listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
       listenSocket.bind((self.host,self.port))
       listenSocket.listen(1)
       
       print 'Server is listening at %s...' % self.port
       while True:
           httpResponse = ""
           clientConn, clientAddr = listenSocket.accept()
           req = clientConn.recv(1024)
           if self.type == "text/html":
               file = open(response)
               httpResponse = """
HTTP/1.1 200 OK

""" + file.read()
           elif self.type == "text/plain":
               httpResponse = """\
HTTP/1.1 200 OK

""" + self.response
        
           clientConn.sendall(httpResponse)
           clientConn.close()

