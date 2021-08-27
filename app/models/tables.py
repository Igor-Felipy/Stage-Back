from enum import unique
from app import db 

class UserLogin(db.Model):
    __tablename__ = "login"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    user_type = db.Column(db.String)
    
    def __init__(self, username, password, user_type):
        self.username = username
        self.password = password
        self.user_type = user_type

    def __repr__(self):
        return "<User %r>" % self.username

    