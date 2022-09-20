from flask import Blueprint, jsonify
from main import db
from models.preferences import Preference
from schemas.preferences_schema import preference_schema, preferences_schema

preferences = Blueprint('preferences',__name__, url_prefix="/preferences")

@preferences.route("/", methods=['GET'])
def get_preferences():
    preference = Preference.query.all()
    result = preferences_schema.dump(preference)
    return jsonify(result)