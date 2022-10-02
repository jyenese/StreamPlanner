from datetime import timedelta
from doctest import debug_script
from flask import Blueprint, jsonify, request
from main import db
from models.user import User
from models.admin import Admin
from models.services import Services
from models.preferences import Preference
from schemas.service_schema import services_schema, service_schema
from schemas.user_schemas import user_schema
from schemas.admin_schema import admin_schema
from schemas.preferences_schema import preference_schema, preferences_schema
from main import bcrypt
from main import jwt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

user = Blueprint('user',__name__, url_prefix="/user")

#The official register, can't use any other features without a user_id, after user is made, token is provided
@user.route('/register', methods=['POST'])
def register_user():
    user_fields = user_schema.load(request.json)
    
    user = User.query.filter_by(username=user_fields["username"]).first()
    if user:
        return {"error":"username already exists"},401
    email = User.query.filter_by(email_address=user_fields["email_address"]).first()
    if email:
        return {"error":"email already exists"}, 401
    user = User(
        username = user_fields['username'],
        email_address = user_fields['email_address'],
        password = bcrypt.generate_password_hash(user_fields['password']).decode("utf-8"),
        dob = user_fields['dob'],
        country = user_fields['country'],
        
    )
    db.session.add(user)
    db.session.commit()
    
    token = create_access_token(identity=str(user.user_id),expires_delta=timedelta(days=1))
    
    return {"username":user.username,"user_id (You will need this ID to add to preferences):":user.user_id, "token":token}, 200

# Logging in with your username and password, if you dont have one it will come up with an error.
# Once logged in you can view your recommendations
@user.route('/login', methods=['POST'])
def login_user():
    user_fields = user_schema.load(request.json)
    user = User.query.filter_by(username=user_fields["username"]).first()
    if not user:
        return {"error": "Wrong Username"},401
    
    if not bcrypt.check_password_hash(user.password, user_fields["password"]):
        return {"error":"Wrong password"}, 401

    token = create_access_token(identity=str(user.user_id), expires_delta=timedelta(days=1))
    
    return {"username":user.username, "token":token}, 200


#Admin login, no register for this user, only created in the hardcode. Has ability to Add/Delete/Update
# Also has the ability to add services to movies.
@user.route('/login/admin', methods=['POST'])
def login_admin():
    admin_fields = admin_schema.load(request.json)
    admin = Admin.query.filter_by(username=admin_fields["username"]).first()
    if not admin:
        return {"error": "Username not found"},401
    
    if not bcrypt.check_password_hash(admin.password, admin_fields["password"]):
        return {"error":"Wrong password"},401

    token = create_access_token(identity="admin", expires_delta=timedelta(days=1))
    
    return {"admin":admin.username, "token":token},200

#Preferences are attatched to the user, so once logged in with your details, you can see your preferences
@user.route("/preferences", methods=['GET'])
@jwt_required()
def get_preferences():
    preference = Preference.query.all()
    result = preferences_schema.dump(preference)
    return jsonify(result),201

#Admin tag needed here, added this in just incase a user has problems seeing what there preferences are,
# If you aren't an admin you will get an error 401, or if the preference ID isnt in the database you will get
# a error 200
@user.route("/preferences/<int:id>", methods=['GET'])
@jwt_required()
def get_preference(id):
    if get_jwt_identity() != "admin":
        return{"error": "You do not have permission to update"}, 401
    preference = Preference.query.get(id)
    if not preference:
        return {"Error":"Preference ID not found"}, 200
    preference = Preference.query.get(id)
    result = preference_schema.dump(preference)
    return jsonify(result),201

#Adding preferences to your account is done via this route, jwt identity links you with your preference_id,
# this is something you will do once you create your account, Posting will be with the fields given bellow.
@user.route("preferences/add", methods=['POST'])
@jwt_required()
def add_preference():
    if not get_jwt_identity():
        return {"error": "User not found"},401
    user_id = get_jwt_identity() 
    user = User.query.get(user_id)
    preference_fields = preference_schema.load(request.json)
    preference = Preference(
        user_id = preference_fields["user_id"],
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
    return jsonify(preference_schema.dump(preference)),201
#This is the PUT request for preferences, which again will be attatched with the user, so you have the ability
# to change your preferences with this request.
#need help changing the int:id to username or something more useful
@user.route("/preferences/update/<int:id>", methods=["PUT"])
@jwt_required()
def preferences_update(id):
    user_id = get_jwt_identity() 
    user = User.query.get(user_id)
    if not user:
        return {"error":"User not found"},401
    preference = Preference.query.get(id)
    preference_fields = preference_schema.load(request.json)
    preference.action = preference_fields["action"]
    preference.adventure = preference_fields["adventure"]
    preference.comedy = preference_fields["comedy"]
    preference.fantasy = preference_fields["fantasy"]
    preference.horror = preference_fields["horror"]
    preference.mystery = preference_fields["mystery"]
    preference.drama = preference_fields["drama"]
    preference.science_fiction = preference_fields["science_fiction"]
    db.session.commit()
    return jsonify(preference_schema.dump(preference)),201
    

# This route shows which services are available on th database, only admins have access to publishing
# these to the database or adding them to MOVIE/TV IDs,
@user.route("/services", methods=['GET'])
def get_services():
    service = Services.query.all()
    result = services_schema.dump(service)
    return jsonify(result),201

# Admin only tag, users shouldn't need access to adding services as theres such a limited amount of them
# This route gives the admin access to adding to the services table, for movies and tv shows to be added to.
@user.route("/services/add", methods=['POST'])
@jwt_required()
def add_service():
    if get_jwt_identity() != "admin":
        return {"error": "You do not have permission to add"},401
    service_fields = service_schema.load(request.json)
    service = Services(
        name = service_fields.get("name"),
        price = service_fields.get("price"),
        description = service_fields.get("description")
    )
    db.session.add(service)
    db.session.commit()
    return jsonify(service_schema.dump(service)),201

#Admin tag, only admins have the ability to delete a service, This function has been added for the purpose
# of maybe one day the company closes the service.
@user.route("/services/delete/<int:id>", methods=['DELETE'])
@jwt_required()
def delete_service(id):
    if get_jwt_identity() != "admin":
        return {"error": "You do not have permission to add"},401
    service = Services.query.get(id)
    if not service:
        return {"error": "Service ID not found"},401
    db.session.delete(service)
    db.session.commit()
    return{"message":"Movie has been deleted from the database"},201

#The update route is also an Admin only section, purpose of use is for potential name change or price change
# easily changed with this Put request.
@user.route("/services/update/<int:id>", methods=["PUT"])
@jwt_required()
def update_service(id):
    if get_jwt_identity() != "admin":
        return{"error": "You do not have permission to update"},401
    service = Services.query.get(id)
    if not service:
        return {"error": "Service ID not found"},401
    
    service_fields = service_schema.load(request.json)
    service.name = service_fields["name"]
    service.price = service_fields["price"]
    service.description = service_fields["description"]
    
    db.session.commit()
    return jsonify(service_schema.dump(service)),201



    