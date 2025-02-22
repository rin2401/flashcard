from flask import Flask, Response, render_template

app = Flask(__name__, template_folder='')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/gmat')
def gmat():
    return render_template('gmat/index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)