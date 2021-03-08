from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

if __name__ == '__main__':
    # 创建初始数据
    db.create_all()
    # 创建一些用户
    # admin = User('admin', 'admin@example.com')
    # guest = User('guest', 'guest@example.com')
    # # 写入到数据库
    # db.session.add(admin)
    # db.session.add(guest)
    # db.session.commit()
    # 访问数据库
    users = User.query.all()
    admin = User.query.filter_by(username='admin').first()
    print(users)
    print(admin)
