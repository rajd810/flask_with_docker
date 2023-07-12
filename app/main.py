from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def index():
    return render_template('about.html')

@app.route('/experience')
def experience():
    return render_template("experience.html")

@app.route('/skills')
def skills():
    return render_template("skills.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5001, debug = True)