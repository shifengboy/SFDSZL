#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:flask_demo.py
@time:2021/01/22
"""


from flask import Flask, escape, url_for, request, session

app = Flask(__name__)
app.secret_key="shifeng"

@app.route('/')
def index():
    return 'index'

@app.route('/login',methods=['GET', 'POST'])
def login():
    res = {
        "method":request.method,
        "url":request.path,
        "args":request.args,
        "form":request.form
    }
    session["username"] = request.args.get('name')
    return res

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

if __name__ == '__main__':
    app.run(debug=True)


