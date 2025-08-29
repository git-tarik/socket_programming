import socket
import threading

# Define host and port
HOST = '127.0.0.1'
PORT = 12345

# Task list assigned to each client
tasks = {
    1: ('add', 10, 5),
    2: ('subtract', 20, 8),
    3: ('multiply', 4, 6),
    4: ('divide', 40, 5),
}

def handle_client(conn, addr, client_id):
    print(f"Client {client_id} connected from {addr}")

    operation, a, b = tasks[client_id]
    message = f"{operation},{a},{b}"
    conn.sendall(message.encode())  # send task

    result = conn.recv(1024).decode()
    print(f"Result from Client {client_id}: {result}")
    conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(4)

    print(f"Server listening on {HOST}:{PORT}")

    client_id = 1
    while client_id <= 4:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr, client_id))
        thread.start()
        client_id += 1

    server.close()

if __name__ == "__main__":
    start_server()
