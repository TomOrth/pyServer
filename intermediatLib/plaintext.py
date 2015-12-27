from server import Server

s = Server("text/plain")
s.listen("0.0.0.0",8888,"hello there world")
