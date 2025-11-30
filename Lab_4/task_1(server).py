import socket

# Налаштування сервера
HOST = '127.0.0.1'  # Localhost (стандартний loopback інтерфейс)
PORT = 65432  # Порт для прослуховування (можна будь-який > 1023)


def start_server():
    # Створюємо сокет (AF_INET = IPv4, SOCK_STREAM = TCP)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Прив'язуємо сокет до адреси та порту
        s.bind((HOST, PORT))
        # Починаємо слухати вхідні з'єднання
        s.listen()
        print(f"Server listening on {HOST}:{PORT}...")

        # accept() блокує виконання, поки хтось не підключиться
        conn, addr = s.accept()

        with conn:
            print(f"Connected by {addr}")
            while True:
                # Читаємо дані (максимум 1024 байти за раз)
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received: {data.decode('utf-8')}")

                # Відправляємо дані назад клієнту (Echo)
                conn.sendall(data)


if __name__ == "__main__":
    start_server()