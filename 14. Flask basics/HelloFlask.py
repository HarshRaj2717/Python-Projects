from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"


@app.route("/page2")
def something():
    return "something on page 2"


@app.route("/username/<name>/<int:number>")
def greet_name(name, number):
    return f"Hi, {name}, here is you number plus 1 = {number+1}"


@app.route("/kitten")
def kitten():
    return '''<h1 style="text-align:center">kittennnnnn</h1>
    <p>you asked for it right !!</p>
    <img src="https://media0.giphy.com/media/njtPBlbYnHAHK/giphy.gif?cid=ecf05e47h0cnwkuv5kj4nvdarfsdaoz2j7etd4nxiawg513z&rid=giphy.gif&ct=g">
    '''


if __name__ == "__main__":
    app.run(debug=True)
