from flask import Blueprint, jsonify
from main import db
from models.price import Price
from schemas.price_schema import price_schema, prices_schema
from flask_jwt_extended import jwt_required

price = Blueprint('prices',__name__, url_prefix="/prices")

@price.route("/", methods=['GET'])
def get_prices():
    price = Price.query.all()
    result = prices_schema.dump(price)
    return jsonify(result)

@price.route("/<int:id>", methods=['GET'])
@jwt_required()
def get_price(id):
    price = Price.query.get(id)
    result = price_schema.dump(price)
    return jsonify(result)