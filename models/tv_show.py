from main import db

class Tv_show(db.Model):
    __tablename__ = "tv_show"
    tv_show_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(255), nullable=False)
    date_added = db.Column(db.Date(), nullable=False)
    netflix = db.Column(db.Boolean)
    disney_plus = db.Column(db.Boolean)
    stan = db.Column(db.Boolean)
    binge = db.Column(db.Boolean)
    appletv = db.Column(db.Boolean)
    foxtel = db.Column(db.Boolean)
    amazon_prime = db.Column(db.Boolean)
