from main import db

class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), nullable=False)
    email_address = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(16), nullable=False)
    dob = db.Column(db.Date())
    country = db.Column(db.String(50), nullable=False)
