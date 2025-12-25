Лабораторна робота №1: Робота з HTTP протоколом, запитами та публічними API

ХІД РОБОТИ

Завдання 1. Отримання курсу валют через Postman [Easy]
Для отримання даних про курс USD за попередній тиждень було використано API Національного банку України.
Метод: GET
URL: https://bank.gov.ua/NBU_Exchange/exchange_site

![task1](https://github.com/user-attachments/assets/3000b36a-308a-4797-bb8d-103cfd9d6188)

Завдання 2. Отримання курсу валют через Python (requests) [Easy]
Реалізовано скрипт task_2.py, який автоматично обчислює дати попереднього тижня та виконує запит до API НБУ за допомогою бібліотеки requests. Отримані дані виводяться в консоль у форматі JSON.

![task2](https://github.com/user-attachments/assets/e5054c6c-c76b-4f66-abfd-0ec593921c58)

Завдання 3. Побудова графіка зміни курсів (matplotlib) [Easy-Medium]
На основі даних, отриманих від API НБУ, було розроблено скрипт task_3.py для візуалізації коливань курсу долара.

![task3](https://github.com/user-attachments/assets/51a85903-d54c-48e3-8e7f-7e8f016ad3e0)

Завдання 4. Взаємодія з Telegram API через Telethon [Medium]
Використовуючи клієнтську бібліотеку Telethon, було реалізовано скрипт task_4.py, який підключається до Telegram через api_id та api_hash.

![task4](https://github.com/user-attachments/assets/f63641ad-c64d-4380-a627-82d2e17a040e)

Завдання 5. Створення Telegram-бота (Telebot) [Hard]
Розроблено чат-бота MyLabBot на базі Telegram Bot API. Бот підтримує наступні команди:
/start або /menu: виводить клавіатуру з командами.
/scream [текст]: перетворює текст у верхній регістр та додає знаки оклику.
/whisper [текст]: відправляє текст у прихованому форматі (спойлер).

![task5](https://github.com/user-attachments/assets/1470de88-ee61-41d7-bbcf-3699682e8fde)
