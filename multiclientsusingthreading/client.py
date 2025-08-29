import socket

HOST = '127.0.0.1'
PORT = 12345

def perform_task(task):
    operation, a, b = task
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        return a / b
    else:
        return 'Unknown operation'

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    data = client.recv(1024).decode()
    operation, a, b = data.split(',')
    a = float(a)
    b = float(b)

    result = perform_task((operation, a, b))
    client.sendall(str(result).encode())

    client.close()

if __name__ == "__main__":
    main()
