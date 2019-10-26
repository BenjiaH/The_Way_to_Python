import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(("192.168.3.59", 30000))
print(client_socket.recv(2048).decode("UTF-8"))