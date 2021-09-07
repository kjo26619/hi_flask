from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/css')
def hello_css():
    return '<h2>css</h2> css'

@app.route('/api/html')
def hello_html():
    return '<h2>html</h2> html'

if __name__ == "__main__":
    app.run()
