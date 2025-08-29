import socket
import time

HOST = '127.0.0.1'
PORT = 12345

def main():
    # ---- Interactive session ----
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print("[CLIENT] Connected to server.")

    print("Type commands like:")
    print("  read data.txt")
    print("  write data.txt Some content")
    print("  exit")

    while True:
        cmd = input(">>> ").strip()
        client.sendall(cmd.encode())
        response = client.recv(4096).decode()
        print(f"[SERVER]: {response}")
        if cmd.startswith("exit"):
            break

    client.close()
    print("[CLIENT] Disconnected.")

    # ---- Scripted session using predefined commands ----
    commands = [
        "read data.txt",
        "write data.txt",   # keep as in your original list
        "exit"
    ]

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print("[CLIENT] Connected to server.")

    for cmd in commands:
        print(f"\n[CLIENT] Sending: {cmd}")
        client.sendall(cmd.encode())
        response = client.recv(4096).decode()
        print(f"[SERVER]: {response}")

        time.sleep(1)  # Just to see responses clearly
        if cmd.startswith("exit"):
            break

    client.close()
    print("\n[CLIENT] Disconnected.")

if __name__ == "__main__":
    main()
