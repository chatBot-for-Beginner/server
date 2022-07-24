from . import db

class User(db.Model):
    id = db.Column(db.String(10), primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    pw = db.Column(db.String(10), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)