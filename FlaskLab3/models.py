from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Array(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    original_array = db.Column(db.String, nullable=False)
    sorted_array = db.Column(db.String, nullable=False)

    def __init__(self, original_array, sorted_array):
        self.original_array = original_array
        self.sorted_array = sorted_array

