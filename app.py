from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about_model')
def about_model():
    return render_template("about_model.html")

if __name__ == "__main__":
    app.run()