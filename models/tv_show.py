from main import db

class Tv_show(db.Model):
    __tablename__ = "tv_show"
    tv_show_id = db.Column(db.Integer, primary_key=True)
    TVA = db.relationship(
        "TVA",
        backref="tv_show"
    )
    title = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(255), nullable=False)
    date_added = db.Column(db.Date(), nullable=False)

