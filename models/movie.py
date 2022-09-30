from main import db

class Movie(db.Model):
    __tablename__ = "movies"
    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(255), nullable=False)
    date_added = db.Column(db.Date(), nullable=False)
    service_id = db.Column(db.Integer,db.ForeignKey("services.service_id"))
    

   