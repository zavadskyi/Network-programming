from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# 1.e.i [Easy] Зберігання у словнику (поки що)
catalog = {
    1: {"id": 1, "name": "T-Shirt", "price": 25.50, "size": "M"},
    2: {"id": 2, "name": "Jeans", "price": 50.00, "size": "L"},
    3: {"id": 3, "name": "Hat", "price": 15.00, "size": "OneSize"}
}

# 1.a.i Ендпоінт /items
@app.route('/items', methods=['GET', 'POST'])
def items_list():
    # 1.c.i GET для зчитування всіх записів
    if request.method == 'GET':
        return jsonify(list(catalog.values()))

    # 1.c.ii POST для створення записів
    elif request.method == 'POST':
        if not request.json:
            abort(400, description="Missing JSON body")

        data = request.json
        new_id = max(catalog.keys()) + 1 if catalog else 1
        data['id'] = new_id

        # Валідація: перевіряємо мінімум 3 параметри (згідно завдання)
        if 'name' not in data or 'price' not in data:
            abort(400, description="Missing required fields (name, price)")

        catalog[new_id] = data
        return jsonify(data), 201

# 1.a.ii Ендпоінт /items/<id>
@app.route('/items/<int:item_id>', methods=['GET', 'PUT', 'DELETE'])
def item_detail(item_id):
    if item_id not in catalog:
        abort(404, description="Item not found")

    # 1.c.i GET для одного запису
    if request.method == 'GET':
        return jsonify(catalog[item_id])

    # 1.c.iii PUT для оновлення запису
    elif request.method == 'PUT':
        if not request.json:
            abort(400, description="Missing JSON body")

        data = request.json
        # Оновлюємо поля
        catalog[item_id].update(data)
        # Гарантуємо, що ID не змінився
        catalog[item_id]['id'] = item_id

        return jsonify(catalog[item_id])

    # 1.c.iv DELETE для видалення записів
    elif request.method == 'DELETE':
        del catalog[item_id]
        return jsonify({"result": "Item deleted"}), 200

if __name__ == '__main__':
    app.run(port=8000, debug=True)