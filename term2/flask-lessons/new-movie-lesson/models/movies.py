from main import db


class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    genre = db.Column(db.String(50))
    length = db.Column(db.String(5))
    year = db.Column(db.String(4))



