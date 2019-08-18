from flask import Flask
import flask

import TelegramClient

app = Flask(__name__, template_folder='./app/templates')


@app.route('/')
def hello_world():
    return flask.render_template('index.html', dir=dir(flask.request.remote_addr), ip=flask.request.remote_addr)


@app.route('/send/<string:person>/<string:text>/')
def send(person, text):
    return flask.json.jsonify(**{'id': 45, 'person': person, 'message': text})


def start(host: str = None, port: int = None, debug: bool = None):
    app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    start()
