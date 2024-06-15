# models.py
from app import db

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    image_url = db.Column(db.String(200), nullable=True)
    user_id = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<ToDo {self.title}>'
