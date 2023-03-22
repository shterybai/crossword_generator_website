from flask import Flask, redirect, url_for, render_template, request, make_response, session
import pdfkit
import requests
# import wkhtmltopdf

# path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
# config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
# pdfkit.from_url("http://google.com", "out.pdf", configuration=config)

app = Flask(__name__)
app.secret_key = "g7r76VFiUyigIy*^RgiOIipghvi7hvuYgU65VJGI&879&3£%AsDIjklb"

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
        response = requests.get(f'https://c2db-109-255-231-194.eu.ngrok.io/request?user_words={combined_words}')
        session["api_data"] = response.json()

        print(response.json())

        # Step 6: return a response to the user
        return render_template("display_crossword.html", crossword=response.json())
    else:
        return render_template("index.html")


@app.route('/filled-crossword-pdf')
def create_filled_pdf():
    if "api_data" in session:
        response = session["api_data"]
    else:
        return redirect(url_for("home"))

    # Render the Jinja template to a string
    rendered = render_template('filled_crossword.html', crossword=response)

    # Convert the rendered HTML to a PDF
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdf = pdfkit.from_string(rendered, False, configuration=config, options={"enable-local-file-access": ""})

    # Create a response object with the PDF as the content
    pdf_response = make_response(pdf)
    pdf_response.headers['Content-Type'] = 'application/pdf'
    pdf_response.headers['Content-Disposition'] = 'attachment; filename=filled_crossword.pdf'
    return pdf_response


@app.route('/empty-crossword-pdf')
def create_empty_pdf():
    if "api_data" in session:
        response = session["api_data"]
    else:
        return redirect(url_for("home"))

    # Render the Jinja template to a string
    rendered = render_template('empty_crossword.html', crossword=response)

    # Convert the rendered HTML to a PDF
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdf = pdfkit.from_string(rendered, False, configuration=config, options={"enable-local-file-access": ""})

    # Create a response object with the PDF as the content
    pdf_response = make_response(pdf)
    pdf_response.headers['Content-Type'] = 'application/pdf'
    pdf_response.headers['Content-Disposition'] = 'attachment; filename=empty_crossword.pdf'
    return pdf_response


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
