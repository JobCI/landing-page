from flask import Flask
from flask import render_template
from flask import send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def send_js(filename):
    return send_from_directory(filename, static_url_path='static')

if __name__ == "__main__":
    app.run(debug=True)
