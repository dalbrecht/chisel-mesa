from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/ping/")
def ping():
    return jsonify({"ping": "pong"})


if __name__ == "__main__":
    app.run(debug=True)