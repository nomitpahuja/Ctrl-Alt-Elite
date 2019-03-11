from flask import Flask
app = Flask(__name__)

@app.route("/output")
def output():
    return "testing"


if __name__ == "__main__":
    app.run()

