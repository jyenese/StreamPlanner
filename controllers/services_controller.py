from flask import Blueprint, jsonify
from main import db
from models.services import Service
from schemas.services_schema import service_schema, services_schema

services = Blueprint('services',__name__, url_prefix="/services")

@services.route("/", methods=['GET'])
def get_services():
    services = Service.query.all()
    result = services_schema.dump(services)
    return jsonify(result)

@services.route("/<int:id>", methods=['GET'])
def get_service(id):
    services = Service.query.get(id)
    result = service_schema.dump(services)
    return jsonify(result)