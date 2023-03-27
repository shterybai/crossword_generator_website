from flask import Flask, redirect, url_for, render_template, request, session
import datetime
from datetime import timedelta
import requests

app = Flask(__name__)
app.secret_key = "g7r76VFiUyigIy*^RgiOIipghvi7hvuYgU65VJGI&879&3£%AsDIjklb"
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(minutes=10)


@app.route("/fyp", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        # Step 3: extract the values of the three input fields
        word1 = request.form['word1']
        word2 = request.form['word2']
        word3 = request.form['word3']

        # Step 4: combine the values of the input fields into a string
        combined_words = f"{word1},{word2},{word3}"
        # return combined_words

        # Step 5: make a GET request to the external API using the combined string
        response = requests.get(f'https://d1cd-109-255-231-194.eu.ngrok.io/request?user_words={combined_words}')
        session["api_data"] = response.json()

        print(response.json())

        # Step 6: return a response to the user
        return render_template("crossword.html", crossword=response.json())
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


# @app.route("/crossword_request", methods=["POST", "GET"])
# def crossword_request():
#     word1 = request.form['word1']
#     word2 = request.form['word2']
#     word3 = request.form['word3']
#
#     # Step 4: combine the values of the input fields into a string
#     combined_words = f"{word1},{word2},{word3}"
#     # return combined_words
#
#     # Step 5: make a GET request to the external API using the combined string
#     response = requests.post(f'https://3eef-109-255-231-194.eu.ngrok.io/request?user_words={combined_words}')
#
#     return response.text


@app.route("/")
def redirect():
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
