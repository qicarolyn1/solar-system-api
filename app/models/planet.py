from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String)
    radius = db.Column(db.Integer)
    description = db.Column(db.Text)
