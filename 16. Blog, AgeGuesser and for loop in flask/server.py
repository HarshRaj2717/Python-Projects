from flask import Flask, render_template
import requests

app = Flask("server")


def guess_functionality(name):
    agify_response = requests.get(f"https://api.agify.io/?name={name}")
    genderize_response = requests.get(f"https://api.genderize.io/?name={name}")
    
    agify_response.raise_for_status()
    genderize_response.raise_for_status()

    age = agify_response.json()["age"]
    gender = genderize_response.json()["gender"]

    return {"age":age, "gender":gender}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/myblog")
def myblog():
    something = "bruh"
    return render_template("myblog.html", thatthing=something)


@app.route("/guess/<name>")
def guess(name):
    guesses = guess_functionality(name)
    return render_template("guess.html", name=name, gender=guesses["gender"], age=guesses["age"])


@app.route("/forloop")
def forloop():
    return render_template("forloop.html")


if __name__ == "__main__":
    app.run(debug=True)
