from flask import Blueprint,jsonify, request
from main import db
from models.tv_show import Tv_show
from models.TVA import TVA
from schemas.tv_show_schemas import tv_show_schema, tv_shows_schema
from schemas.TVA_schema import tva_schema, tvas_schema
from flask_jwt_extended import jwt_required, get_jwt_identity

tv_shows = Blueprint('tv_shows',__name__, url_prefix="/tv_show")

#Shows a list of all TV shows.
@tv_shows.route("/", methods=['GET'])
def get_tv_shows():
    tv_shows = Tv_show.query.all()
    result = tv_shows_schema.dump(tv_shows)
    return jsonify(result)

#Search the database for a certain TV_show_id (title), and if there isnt one, give an error.
@tv_shows.route("/<int:id>", methods=['GET'])
def get_tv_show(id):
    tv_shows = Tv_show.query.get(id)
    if not tv_shows:
        return {"error": "tv_show not found"}
    result = tv_show_schema.dump(tv_shows)
    return jsonify(result)

#Asking for Admin ID, then if given, you have access to add to the database a 'TV show'
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

#Asking for Admin ID, then if given, you have access to delete the TV show
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

#Asking for Admin ID, then if given, you have access to update the TV show
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

#Showing an example of how it would work, The ID of TV show with the service its on
@tv_shows.route("/available", methods=['GET'])
def get_tv_available():
    list = TVA.query.all()
    result = tvas_schema.dump(list)
    return jsonify(result)