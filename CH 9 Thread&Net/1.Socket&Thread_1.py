import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.bind(("192.168.3.59", 30000))
s.listen
while True:
    c, addr = s.accept()
    print(addr)
    c.send("我是服务端！".decode("UTF-8"))
    c.close
