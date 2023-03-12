from flask import Flask, url_for
from waitress import serve
app = Flask(__name__)


@app.route('/')
def index():
    return f'''<html>
    Привет от приложения Flask
    <br>
    <img src="{url_for('static', filename='smeshariki.png')}"
    </html>
    '''


if __name__ == '__main__':
    # app.run(port=8080, host='127.0.0.1')
    serve(app, host='0.0.0.0', port=5000)