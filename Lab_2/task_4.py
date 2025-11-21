from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/headers")
def headers_handler():
    content_type = request.headers.get("Content-Type")

    if content_type == "application/json":
        return {"currency": "USD", "value": 41.5}
    elif content_type == "application/xml":
        xml_content = "<data><currency>USD</currency><value>41.5</value></data>"
        return Response(xml_content, mimetype="application/xml")
    else:
        return "Currency: USD - 41.5"

if __name__ == "__main__":
    app.run(port=8000)