from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/fyp")
def home():
    return render_template("index.html")


@app.route("/")
def redirect():
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
