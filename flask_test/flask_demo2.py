#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:flask_demo2.py
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
    # return '{}\'s profile'.format(escape(username))
    return f'{username}\'s profile'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    # return 'Subpath %s' % escape(subpath)
    return 'Subpath %s' % subpath

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

if __name__ == '__main__':
    app.run(debug=True)
    # print(__name__)

