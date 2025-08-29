import socket

HOST = '127.0.0.1'
PORT = 12345

tasks = {
    1: ('add', 10, 5),
    2: ('subtract', 20, 8),
    3: ('multiply', 4, 6),
    4: ('divide', 40, 5),
}

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(4)

    print(f"Server listening on {HOST}:{PORT}")

    for client_id in range(1, 5):
        conn, addr = server.accept()
        print(f"Client {client_id} connected from {addr}")

        operation, a, b = tasks[client_id]
        message = f"{operation},{a},{b}"
        conn.sendall(message.encode())

        result = conn.recv(1024).decode()
        print(f"Result from Client {client_id}: {result}")
        conn.close()

    server.close()

if __name__ == "__main__":
    main()
