from flask import Flask, request, Response, abort

app = Flask(__name__)


@app.route("/simple_get", methods=["GET"])
def simple_get():
    format = request.args.get("format", None)

    if format is None:
        abort(404)

    if format.lower() == "text":
        return "This is a text."
    elif format.lower() == "json":
        return {"data": "This is json data"}
    elif format.lower() == "image":
        with open("image.jpg", "rb") as f:
            frame = f.read()
        return Response(frame, mimetype="image/jpeg")


@app.route("/json_post", methods=["POST"])
def json_post():
    json_data = request.get_json()
    text = request.get_data()

    print(f"JSON: {json_data}")
    print(f"TEXT: {text}")

    return "Json get."


@app.route("/form_post", methods=["POST"])
def form_post():
    test = request.form.get("test", type=str)
    f = request.files.get("file")
    print(test)
    if f:
        print(f)

    return "Form data get"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)
