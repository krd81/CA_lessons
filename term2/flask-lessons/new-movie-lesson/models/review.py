from main import db


class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='reviews')

    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)
    movie = db.relationship('Movie', back_populates='reviews')

