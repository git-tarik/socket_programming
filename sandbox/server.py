import socket
import os

HOST = '127.0.0.1'
PORT = 12345
BASE_DIR = 'files'

# Sandbox: Define allowed operations
ALLOWED_OPERATIONS = {
    "read":False,
    "write": False,
    "exit": False
}

def sandbox_handler(request):
    parts = request.strip().split(' ', 2)
    command = parts[0]

    # Unknown command
    if command not in ALLOWED_OPERATIONS:
        return f"Error: Unknown command '{command}'"

    # Denied by sandbox
    if not ALLOWED_OPERATIONS[command]:
        return f"Denied: Operation '{command}' is not allowed by sandbox"

    # Handle allowed commands
    if command == "read":
        if len(parts) < 2:
            return "Error: No filename provided"
        filename = parts[1]
        filepath = os.path.join(BASE_DIR, filename)
        try:
            with open(filepath, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return "Error: File not found"

    elif command == "write":
        if len(parts) < 3:
            return "Error: Invalid write format"
        filename = parts[1]
        content = parts[2]
        filepath = os.path.join(BASE_DIR, filename)
        with open(filepath, 'a') as f:
            f.write(content + "\n")
        return "Write successful"

    elif command == "exit":
        return "Session ended by client"

    return "Unhandled command"

def main():
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"[SERVER] Listening on {HOST}:{PORT}")

        conn, addr = s.accept()
        with conn:
            print(f"[SERVER] Connected by {addr}")
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break

                print(f"[SERVER] Received: {data}")
                response = sandbox_handler(data)
                conn.sendall(response.encode())

                if data.strip().startswith("exit"):
                    break

        print("[SERVER] Connection closed")

if __name__ == "__main__":
    main()
