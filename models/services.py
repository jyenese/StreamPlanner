from main import db

class Service(db.Model):
    __tablename__ = "services"
    service_id = db.Column(db.Integer, primary_key=True)
    netflix = db.Column(db.Boolean)
    disney_plus = db.Column(db.Boolean)
    stan = db.Column(db.Boolean)
    binge = db.Column(db.Boolean)
    appletv = db.Column(db.Boolean)
    foxtel = db.Column(db.Boolean)
    amazon_prime = db.Column(db.Boolean)
