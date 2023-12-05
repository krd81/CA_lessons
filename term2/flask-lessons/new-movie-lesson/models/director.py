from main import db


class Director(db.Model):
    __tablename__ = "directors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    country = db.Column(db.String(50))

    # movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)
    movies = db.relationship('Movie', back_populates='director')


