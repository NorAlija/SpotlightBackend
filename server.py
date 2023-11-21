from flask import Flask,request, make_response

app = Flask(__name__)


data = []
@app.route("/save", methods=["POST"])
def save_images():
    data.append(request.json)
    return str(200)

@app.route("/all", methods=["GET"])
def get_img():
    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

    