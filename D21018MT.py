import string
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def base_route():
    return "DEMD MidTerm - D21018"

@app.route("/<name>")
def print_name(name):
    return f"Welcome {name}"

if __name__ == "__main__":
    app.run(debug=True,port=8080)