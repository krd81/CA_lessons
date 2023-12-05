from main import db


class Actor(db.Model):
    __tablename__ = "actors"

    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(50))
    l_name = db.Column(db.String(50))
    gender = db.Column(db.String(15))
    country = db.Column(db.String(50))
    dob = db.Column(db.Date())

    cast = db.relationship('Cast', back_populates='actors')



