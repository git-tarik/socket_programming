import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 12345))
server.listen(1)
print("Server is listening...")

client_socket, addr = server.accept()
print(f"Connection from {addr}")
client_socket.sendall(b"Hello from server!")
client_socket.close()
