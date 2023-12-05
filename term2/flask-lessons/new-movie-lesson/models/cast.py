from main import db


class Cast(db.Model):
    __tablename__ = "cast"

    id = db.Column(db.Integer, primary_key=True)

    actors_id = db.Column(db.Integer, db.ForeignKey('actors.id'), nullable=False)
    actors = db.relationship('Actor', back_populates='cast')

    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)
    movie = db.relationship('Movie', back_populates='cast')

