from flask import Flask, request

app = Flask(__name__)

@app.route("/currency")
def get_currency():
    key = request.args.get("key")

    if key == "USD":
        return "USD - 41.5"
    elif key == "EUR":
        return "EUR - 45.2"
    elif key == "PLN":
        return "PLN - 10.5"
    else:
        return "Unknown currency or missing key"

if __name__ == "__main__":
    app.run(port=8000)