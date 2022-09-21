from main import db
from sqlalchemy.sql import expression
active = db.Column(db.Boolean, server_default=expression.true(), nullable=False)

class Movie(db.Model):
    __tablename__ = "movies"
    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(255), nullable=False)
    date_added = db.Column(db.Date(), nullable=False)
    netflix = db.Column(db.Boolean)
    netflix = db.Column(db.Boolean)
    disney_plus = db.Column(db.Boolean)
    stan = db.Column(db.Boolean)
    binge = db.Column(db.Boolean)
    appletv = db.Column(db.Boolean)
    foxtel = db.Column(db.Boolean)
    amazon_prime = db.Column(db.Boolean)
