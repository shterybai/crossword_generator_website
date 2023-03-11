from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/fyp", methods=["POST", "GET"])
def home():
    if request.method == "POST":

    else:
        return render_template("index.html")


@app.route("/")
def redirect():
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
