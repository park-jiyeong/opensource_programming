from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "message": "Welcome to Flask Blog Service",
        "status": "running"
    })


@app.route("/home")
def home():
    return jsonify({
        "page": "home",
        "description": "This is the home endpoint of the Flask Blog API"
    })


if __name__ == "__main__":
    app.run(debug=True)