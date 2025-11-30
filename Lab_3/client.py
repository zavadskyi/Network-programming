import requests

# Налаштування
BASE_URL = "http://127.0.0.1:8000/items"
AUTH = ('admin', 'secret')  # Логін та пароль для Basic Auth

def print_response(response):
    print(f"Status: {response.status_code}")
    try:
        print(f"Body: {response.json()}")
    except:
        print(f"Body: {response.text}")
    print("-" * 20)

# 1. GET - Отримати список усіх товарів
print("1. GET ALL ITEMS")
response = requests.get(BASE_URL, auth=AUTH)
print_response(response)

# 2. POST - Додати новий товар
print("2. ADD NEW ITEM (Sneakers)")
new_item = {
    "name": "Sneakers",
    "price": 85.00,
    "size": "42"
}
response = requests.post(BASE_URL, json=new_item, auth=AUTH)
print_response(response)
# Отримуємо ID створеного товару
created_id = response.json().get('id')

# 3. GET <id> - Отримати конкретний товар
if created_id:
    print(f"3. GET ITEM ID {created_id}")
    response = requests.get(f"{BASE_URL}/{created_id}", auth=AUTH)
    print_response(response)

    # 4. PUT - Оновити ціну товару
    print(f"4. UPDATE ITEM ID {created_id} (Price -> 99.99)")
    update_data = {"price": 99.99}
    response = requests.put(f"{BASE_URL}/{created_id}", json=update_data, auth=AUTH)
    print_response(response)

    # 5. DELETE - Видалити товар
    print(f"5. DELETE ITEM ID {created_id}")
    response = requests.delete(f"{BASE_URL}/{created_id}", auth=AUTH)
    print_response(response)

    # Перевірка видалення
    print(f"6. CHECK DELETE (Expect 404)")
    response = requests.get(f"{BASE_URL}/{created_id}", auth=AUTH)
    print_response(response)