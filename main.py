from flask import Flask, redirect, url_for, render_template, request, session
import datetime
from datetime import timedelta
import json
import requests

app = Flask(__name__)
app.secret_key = "g7r76VFiUyigIy*^RgiOIipghvi7hvuYgU65VJGI&879&3£%AsDIjklb"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)


@app.route("/fyp", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        try:
            word1 = request.form['word1']
            word2 = request.form['word2']
            word3 = request.form['word3']

            combined_words = f"{word1},{word2},{word3}"

            response = requests.get(f'https://667d-109-255-231-194.eu.ngrok.io/request?user_words={combined_words}')
            session["api_data"] = response.json()

            print(response.json())

            return render_template("crossword.html", crossword=response.json())
        except json.JSONDecodeError:
            # If a JSONDecodeError occurs, raise a custom exception
            raise InvalidDataException('Invalid JSON data')
    elif "api_data" in session:
        response = session["api_data"]
        return render_template("crossword.html", crossword=response)
    else:
        return render_template("index.html")


@app.route('/filled_crossword')
def filled_crossword():
    if "api_data" in session:
        response = session["api_data"]
    else:
        return redirect(url_for("home"))

    return render_template('filled_crossword.html', crossword=response)


@app.route('/empty_crossword')
def empty_crossword():
    if "api_data" in session:
        response = session["api_data"]
    else:
        return redirect(url_for("home"))

    return render_template('empty_crossword.html', crossword=response)


class InvalidDataException(Exception):
    def __init__(self, message):
        self.message = message


@app.errorhandler(InvalidDataException)
def handle_invalid_data_error(error):
    # Render the error template with the error message
    return render_template('error.html', message=error.message), 400


@app.route('/')
def redirect():
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
