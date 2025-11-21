from flask import Flask, request

app = Flask(__name__)

@app.route("/save_post", methods=["POST"])
def save_post_data():
    data = request.get_data(as_text=True)

    with open("saved_data.txt", "a", encoding="utf-8") as f:
        f.write(data + "\n")

    return "Data saved to file successfully"

if __name__ == "__main__":
    app.run(port=8000)