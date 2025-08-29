import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 12345))
data = client.recv(1024)
print("Received:", data.decode())
client.close()
