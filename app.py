from flask import Flask, render_template
'''for test'''
from flask import request
from flask import make_response
from flask_script import Manager
import time

app = Flask(__name__)
handler = Manager(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/time')
def current_t():
    return '<p>time: %s</p>' %time.asctime(time.localtime(time.time()))


@app.route('/<name>')
def render(name):
    return render_template('index.html', name_place=name)


@app.route('/test')
def test_req():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent


@app.route('/test/response')
def test_rsp():
    response = make_response('<h1> this document is carries a cookie</h1>')
    response.set_cookie('cookie1', 'qwe')
    return response


if __name__ == '__main__':
    handler.run()
