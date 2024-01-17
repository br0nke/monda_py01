from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    vardas = "Studentas"
    return render_template('index.html', vardas=vardas)

app.run()