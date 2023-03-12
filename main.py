from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/fyp", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        # Step 3: extract the values of the three input fields
        word1 = request.form['word1']
        word2 = request.form['word2']
        word3 = request.form['word3']

        # Step 4: combine the values of the input fields into a string
        combined_words = f"{word1},{word2},{word3}"
        return combined_words

        # Step 5: make a POST request to the external API using the combined string
        # response = requests.post('https://external-api.com', data={'words': combined_words})

        # Step 6: return a response to the user
        # return response.text
    else:
        return render_template("index.html")


@app.route("/")
def redirect():
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
