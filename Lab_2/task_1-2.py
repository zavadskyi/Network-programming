from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

if __name__ == '__main__':
    print("Starting server on http://127.0.0.1:8000")
    app.run(port=8000, debug=True)