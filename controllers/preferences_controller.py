from flask import Blueprint, jsonify
from main import db
from models.preferences import Preference
from schemas.preferences_schema import preference_schema, preferences_schema
from flask_jwt_extended import jwt_required

preferences = Blueprint('preferences',__name__, url_prefix="/preferences")

@preferences.route("/", methods=['GET'])
@jwt_required()
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