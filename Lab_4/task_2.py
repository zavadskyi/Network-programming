import socket

HOST = '127.0.0.1'
PORT = 65432


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening constantly on {HOST}:{PORT}...")

        # Головний цикл сервера: працюємо постійно
        while True:
            # Чекаємо на нове з'єднання
            conn, addr = s.accept()

            with conn:
                print(f"Connected by {addr}")
                # Цикл обробки даних від конкретного клієнта
                while True:
                    data = conn.recv(1024)
                    if not data:
                        # Клієнт відключився
                        break
                    print(f"Received: {data.decode('utf-8')}")
                    conn.sendall(data)

                print(f"Connection with {addr} closed. Waiting for next client...")


if __name__ == "__main__":
    start_server()