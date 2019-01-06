from flask import Flask
'''for test'''
from flask import request
from flask import make_response
from flask_script import Manager

app = Flask(__name__)
handler = Manager(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


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
