from main import db

class Movie(db.Model):
    __tablename__ = "movies"
    movie_id = db.Column(db.Integer, primary_key=True)
    MA = db.relationship(
        "MA",
        backref="movies"
    )
    title = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(255), nullable=False)
    date_added = db.Column(db.Date(), nullable=False)
    

   