# Database models
from . import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), unique=True, nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    genres = db.Column(db.String(500), nullable=True)
    vote_average = db.Column(db.Float, nullable=True)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)
    user_comments = db.relationship('UserComment', backref='movie', lazy=True)

class UserComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    comment = db.Column(db.String(250), nullable=True)
