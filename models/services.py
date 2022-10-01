from main import db

class Services(db.Model):
    __tablename__ = "services"
    service_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer)
    description = db.Column(db.String(255), nullable=False)
    movies = db.relationship(
        "Movie",
        backref="service"
    )
    tv_show = db.relationship(
        "Tv_show",
        backref="service"
    )
    