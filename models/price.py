from main import db

class Price(db.Model):
    __tablename__ = "price"
    price_id = db.Column(db.Integer, primary_key=True)
    netflix = db.Column(db.Integer())
    stan = db.Column(db.Integer())
    disney_plus = db.Column(db.Integer())
    binge = db.Column(db.Integer())
    apple_tv = db.Column(db.Integer())
    foxtel = db.Column(db.Integer())
    amazon_prime = db.Column(db.Integer())
    date = db.Column(db.Date())
    