import socket

# Адреса сервера, до якого підключаємось
HOST = '127.0.0.1'
PORT = 65432


def start_client():
    # Створюємо сокет
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Підключаємось до сервера
        s.connect((HOST, PORT))

        # Відправляємо повідомлення (треба конвертувати в bytes)
        message = "Hello, Socket World!"
        print(f"Sending: {message}")
        s.sendall(message.encode('utf-8'))

        # Чекаємо відповідь від сервера
        data = s.recv(1024)

    print(f"Received back from server: {data.decode('utf-8')}")


if __name__ == "__main__":
    start_client()