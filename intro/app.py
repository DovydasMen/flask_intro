from flask import Flask, render_template, request

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p> Hello, World!</p>"

# @app.route("/another/")
# def godbye_world():
#     return "<p> Goodbye, World!</p>"

# @app.route("/<name>")
# def user(name):
#     return f"Hello, {name}"

# @app.route("/calc")
# def calc():
#     return render_template("calc.html")

# @app.route("/name")
# def names():
#     names = ["Jonas", "Antanas", "Petras"]
#     return render_template("name.html", my_list=names)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        return render_template("greetings.html", name=name)
    else:
        return render_template("login.html")


@app.route("/repeater", methods=["GET", "POST"])
def repeater():
    if request.method == "POST":
        name = request.form["name"]
        return render_template("repeater.html", name=name)
    else:
        return render_template("login.html")


@app.route("/year")
def year():
    return render_template("leap_year.html")


if __name__ == "__main__":
    app.run(debug=True, port=7000)
