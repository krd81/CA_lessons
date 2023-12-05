from main import db


class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    genre = db.Column(db.String(50))
    length = db.Column(db.String(5))
    year = db.Column(db.String(4))

    director_id = db.Column(db.Integer, db.ForeignKey('directors.id'), nullable=False)
    director = db.relationship('Director', back_populates='movies')

    reviews = db.relationship('Review', back_populates='movie')

    cast = db.relationship('Cast', back_populates='movie')

