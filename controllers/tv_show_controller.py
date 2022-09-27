from flask import Blueprint,jsonify, request
from main import db
from models.tv_show import Tv_show
from schemas.tv_show_schemas import tv_show_schema, tv_shows_schema
from flask_jwt_extended import jwt_required, get_jwt_identity

tv_shows = Blueprint('tv_shows',__name__, url_prefix="/tv_show")

@tv_shows.route("/", methods=['GET'])
def get_tv_shows():
    tv_shows = Tv_show.query.all()
    result = tv_shows_schema.dump(tv_shows)
    return jsonify(result)

@tv_shows.route("/<int:id>", methods=['GET'])
def get_tv_show(id):
    tv_shows = Tv_show.query.get(id)
    if not tv_shows:
        return {"error": "tv_show not found"}
    result = tv_show_schema.dump(tv_shows)
    return jsonify(result)

@tv_shows.route("/", methods=['POST'])
@jwt_required()
def add_tv_show():
    if get_jwt_identity() != "admin":
        return {"error": "You do not have permission to add"}
    tv_show_fields = tv_show_schema.load(request.json)
    tv_show = Tv_show(
        title = tv_show_fields['title'],
        genre = tv_show_fields['genre'],
        date_added = tv_show_fields['date_added'],
    )
    db.session.add(tv_show)
    db.session.commit()
    return jsonify(tv_show_schema.dump(tv_show))

@tv_shows.route("/<int:id>", methods=['DELETE'])
@jwt_required()
def delete_tv_show(id):
    if get_jwt_identity() != "admin":
        return {"error": "You do not have permission to delete"}
    tv_show = Tv_show.query.get(id)
    if not tv_show:
        return {"Error":"Tv_show ID not found"}
    
    db.session.delete(tv_show)
    db.session.commit() 
    return {"message":"TV Show removed"}

@tv_shows.route("/<int:id>", methods=['PUT'])
@jwt_required()
def update_tv_show(id):
    if get_jwt_identity() != "admin":
        return {"error": "You do not have permission to update"}
    tv_show = Tv_show.query.get(id)
    if not tv_show:
        return {"Error":"TV Show ID not found"}
    
    tv_show_fields = tv_show_schema.load(request.json)
    
    tv_show.title = tv_show_fields['title']
    tv_show.genre = tv_show_fields['genre']
    tv_show.date_added = tv_show_fields['date_added']
    
    db.session.commit()
    return jsonify(tv_show_schema.dump(tv_show))