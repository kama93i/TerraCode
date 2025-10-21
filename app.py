from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    with open("templates/index.html", encoding="UTF-8") as f:
        content = f.read()
        return Response(content, content_type="text/html; charset=utf-8")

@app.route('/contact', methods=['POST'])
def contact_form():
    email = request.form.get("femail")
    message = request.form.get("ftext")

    if not email or not message:
        return "Ha habido un Eror", 400

    print(f"{email} - {message}")
    return "Mensaje recibido"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)