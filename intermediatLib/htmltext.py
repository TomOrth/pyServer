from server import Server

s = Server("text/html")
s.listen("0.0.0.0",8888,"hello.html")
