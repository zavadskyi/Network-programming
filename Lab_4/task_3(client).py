import socket
import os

HOST = '127.0.0.1'
PORT = 65432
FILENAME = 'my_data.txt'  # Ім'я файлу, який будемо відправляти


def send_file():
    # Перевіримо, чи існує файл перед відправкою
    if not os.path.exists(FILENAME):
        print(f"Error: File '{FILENAME}' not found! Create it first.")
        return

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"Connecting to {HOST}:{PORT}...")
        s.connect((HOST, PORT))

        print(f"Sending file '{FILENAME}'...")

        # Відкриваємо файл для читання (rb - read binary)
        with open(FILENAME, 'rb') as f:
            # Читаємо і відправляємо файл шматочками
            chunk = f.read(1024)
            while chunk:
                s.sendall(chunk)
                chunk = f.read(1024)

        print("File sent successfully.")


if __name__ == "__main__":
    # Створимо тестовий файл автоматично, якщо його немає
    if not os.path.exists(FILENAME):
        with open(FILENAME, 'w') as f:
            f.write("This is a test file sent via Python Sockets.\nLine 2.\nLine 3.")
        print(f"Created dummy file '{FILENAME}' for testing.")

    send_file()