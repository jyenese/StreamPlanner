from main import db
#TVA = TV Availability
class TVA(db.Model):
    __tablename__ = "tv_availability"
    TVA_id = db.Column(db.Integer, primary_key=True)
    tv_show_id = db.Column(db.Integer, db.ForeignKey("tv_show.tv_show_id"))
    service_id = db.Column(db.Integer, db.ForeignKey("services.service_id"))
   