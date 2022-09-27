from main import db
#MA = Movie Availability
class MA(db.Model):
    __tablename__ = "movie_availability"
    MA_id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.movie_id"))
    service_id = db.Column(db.Integer, db.ForeignKey("services.service_id"))

    