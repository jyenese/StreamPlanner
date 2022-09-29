from datetime import timedelta
from doctest import debug_script
from flask import Blueprint, jsonify, request
from main import db
from models.user import User
from models.admin import Admin
from models.services import Services
from schemas.service_schema import services_schema, service_schema
from schemas.user_schemas import user_schema
from schemas.admin_schema import admin_schema
from main import bcrypt
from main import jwt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

auth = Blueprint('auth',__name__, url_prefix="/auth")

@auth.route('/register', methods=['POST'])
def register_user():
    user_fields = user_schema.load(request.json)
    
    user = User.query.filter_by(username=user_fields["username"]).first()
    if user:
        return {"error":"username already exists"}
    email = User.query.filter_by(email_address=user_fields["email_address"]).first()
    if email:
        return {"error":"email already exists"}
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
    
    return {"username":user.username, "token":token}

@auth.route('/login', methods=['POST'])
def login_user():
    user_fields = user_schema.load(request.json)
    user = User.query.filter_by(username=user_fields["username"]).first()
    if not user:
        return {"error": "Username not found"}
    
    if not bcrypt.check_password_hash(user.password, user_fields["password"]):
        return {"error":"Wrong password"}

    token = create_access_token(identity=str(user.user_id), expires_delta=timedelta(days=1))
    
    return {"username":user.username, "token":token}



@auth.route('/login/admin', methods=['POST'])
def login_admin():
    admin_fields = admin_schema.load(request.json)
    admin = Admin.query.filter_by(username=admin_fields["username"]).first()
    if not admin:
        return {"error": "Username not found"}
    
    if not bcrypt.check_password_hash(admin.password, admin_fields["password"]):
        return {"error":"Wrong password"}

    token = create_access_token(identity="admin", expires_delta=timedelta(days=1))
    
    return {"admin":admin.username, "token":token}

@auth.route("/services", methods=['GET'])
def get_services():
    service = Services.query.all()
    result = services_schema.dump(service)
    return jsonify(result)

@auth.route("/services/add", methods=['POST'])
@jwt_required()
def add_service():
    if get_jwt_identity() != "admin":
        return {"error": "You do not have permission to add"}
    service_fields = service_schema.load(request.json)
    service = Services(
        service_id = service_fields.get("id"),
        name = service_fields.get("name"),
        price = service_fields.get("price"),
        description = service_fields.get("description")
    )
    db.session.add(service)
    db.session.commit()
    return jsonify(service_schema.dump(service))

@auth.route("/services/delete/<int:id>", methods=['DELETE'])
@jwt_required()
def delete_service(id):
    if get_jwt_identity() != "admin":
        return {"error": "You do not have permission to add"}
    service = Services.query.get(id)
    if not service:
        return {"error": "Service ID not found"}
    db.session.delete(service)
    db.session.commit()
    return{"message":"Movie has been deleted from the database"}

@auth.route("/services/update/<int:id>", methods=["PUT"])
@jwt_required()
def update_service(id):
    if get_jwt_identity() != "admin":
        return{"error": "You do not have permission to update"}
    service = Services.query.get(id)
    if not service:
        return {"error": "Service ID not found"}
    
    service_fields = service_schema.load(request.json)
    service.name = service_fields["name"]
    service.price = service_fields["price"]
    service.description = service_fields["description"]
    
    db.session.commit()
    return jsonify(service_schema.dump(service))