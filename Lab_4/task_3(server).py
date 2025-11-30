import socket

HOST = '127.0.0.1'
PORT = 65432


def start_file_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"File Server listening on {HOST}:{PORT}...")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}. Receiving file...")

                # Відкриваємо файл для запису (wb - write binary, щоб точно зберегти формат)
                with open('received_file.txt', 'wb') as f:
                    while True:
                        # Читаємо дані порціями по 1024 байти
                        data = conn.recv(1024)
                        if not data:
                            # Якщо даних немає - передача завершена
                            break
                        # Записуємо отриману порцію у файл
                        f.write(data)

                print("File received and saved as 'received_file.txt'")
                print("Waiting for next connection...")


if __name__ == "__main__":
    start_file_server()