from flask import jsonify, render_template, request
import socket

from js_example import app


@app.route('/', defaults={'js': 'plain'})
@app.route('/<any(plain, jquery, fetch):js>')
def index(js):
    hostname = socket.gethostname()
    return render_template('{0}.html'.format(js), js=js, hostname=hostname)


@app.route('/add', methods=['POST'])
def add():
    a = request.form.get('a', 0, type=float)
    b = request.form.get('b', 0, type=float)
    return jsonify(result=a + b)
