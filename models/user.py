from main import db

class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    email_address = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    dob = db.Column(db.Date())
    country = db.Column(db.String(), nullable=False)
