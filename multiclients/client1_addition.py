import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 12345))

    data = client.recv(1024).decode()
    _, a, b = data.split(',')
    result = float(a) + float(b)

    client.sendall(str(result).encode())
    client.close()

if __name__ == "__main__":
    main()
