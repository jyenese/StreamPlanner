from flask import Blueprint, jsonify
from main import db
from models.user import User
from schemas.user_schemas import user_schema, users_schema
user = Blueprint('users',__name__, url_prefix="/users")

@user.route("/", methods=['GET'])
def get_users():
    user = User.query.all()
    result = users_schema.dump(user)
    return jsonify(result)

@user.route("/<int:id>", methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    result = user_schema.dump(user)
    return jsonify(result)