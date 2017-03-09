from flask import Flask, jsonify
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    data=[
        {'name': 'Chuck Norris', 'power': 'Infinity'},
        {'name': 'Bruce Lee', 'power': 9000},
        {'name': 'Jackie Chan', 'power': 7000},
        {'name': 'Jet Li', 'power': 8000},
    ]
    return render_template('index.html', data=data)
