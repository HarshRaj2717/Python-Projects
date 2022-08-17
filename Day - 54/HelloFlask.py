from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"


@app.route("/page2")
def something():
    return "something on page 2"


if __name__ == "__main__":
    app.run()
