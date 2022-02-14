from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def main():
    return render_template("index.html")


@app.route('/formResults', methods=["POST"])
def formResults():
    session["person"] = request.form
    return redirect("/results")

@app.route('/results')
def results():
    name = session["person"]["name"]
    location = session["person"]["location"]
    language = session["person"]["language"]
    text = session["person"]["text"]

    return render_template("results.html", name = name, location = location, language = language, text = text)








if __name__=="__main__":
    app.run(debug=True)
