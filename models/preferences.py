from main import db

class Preference(db.Model):
    __tablename__ = "preferences"
    preference_id = db.Column(db.Integer, primary_key=True)
    action = db.Column(db.Boolean)
    adventure = db.Column(db.Boolean)
    comedy = db.Column(db.Boolean)
    fantasy = db.Column(db.Boolean)
    horror = db.Column(db.Boolean)
    mystery = db.Column(db.Boolean)
    drama = db.Column(db.Boolean)
    science_fiction = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))