from flask import Blueprint, jsonify, request
from main import db
from models.preferences import Preference
from models.user import User
from schemas.preferences_schema import preference_schema, preferences_schema
from flask_jwt_extended import jwt_required, get_jwt_identity

preferences = Blueprint('preferences',__name__, url_prefix="/preferences")

@preferences.route("/", methods=['GET'])
# @jwt_required()
def get_preferences():
    preference = Preference.query.all()
    result = preferences_schema.dump(preference)
    return jsonify(result)

@preferences.route("/<int:id>", methods=['GET'])
@jwt_required()
def get_preference(id):
    preference = Preference.query.get(id)
    result = preference_schema.dump(preference)
    return jsonify(result)

@preferences.route("/add", methods=['POST'])
@jwt_required()
def add_preference():
    user_id = get_jwt_identity() 
    user = User.query.get(user_id)
    if not user:
        return {"error":"User not found"}
    
    preference_fields = preference_schema.load(request.json)
    preference = Preference(
        action = preference_fields["action"],
        adventure = preference_fields["adventure"],
        comedy = preference_fields["comedy"],
        fantasy = preference_fields["fantasy"],
        horror = preference_fields["horror"],
        mystery = preference_fields["mystery"],
        drama = preference_fields["drama"],
        science_fiction = preference_fields["science_fiction"],  
    )
    db.session.add(preference)
    db.session.commit()
    return jsonify(preference_schema.dump(preference))

