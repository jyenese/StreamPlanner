from flask import Blueprint,jsonify, request
from main import db
from models.tv_show import Tv_show
from models.user import User
from schemas.tv_show_schemas import tv_show_schema, tv_shows_schema
from schemas.preferences_schema import preferences_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas.service_schema import service_schema, services_schema
from models.services import Services

tv_shows = Blueprint('tv_shows',__name__, url_prefix="/tv_show")

#Shows a list of all TV shows.
@tv_shows.route("/", methods=['GET'])
def get_tv_shows():
    if request.query_string:
        if request.args.get('genre'):
            filtered = Tv_show.query.filter_by(genre=request.args.get('genre'))
            result = tv_shows_schema.dump(filtered)
            return jsonify(result)
        if request.args.get('title'):
            filtered = Tv_show.query.filter_by(title=request.args.get('title'))
            result = tv_shows_schema.dump(filtered)
            return jsonify(result)
        if request.args.get('date_added'):
            filtered = Tv_show.query.filter_by(date_added=request.args.get('date_added'))
            result = tv_shows_schema.dump(filtered)
            return jsonify(result)
        else:
            return {"Error":"No TV show found based on your search."}
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
        service_id = tv_show_fields['service_id'],
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
    tv_show.service_id = tv_show_fields['service_id']
    
    db.session.commit()
    return jsonify(tv_show_schema.dump(tv_show))

#Showing an example of how it would work, The ID of TV show with the service its on
@tv_shows.route("/recommendations", methods=['GET'])
@jwt_required()
def get_tv_recommendations():
    if not get_jwt_identity():
        return {"error": "User not found"}
    user_id = get_jwt_identity() 
    user = User.query.get(user_id)
    tv_shows = {}
    preferences = preferences_schema.dump(user.preferences)
    preference = preferences[0]
    if preference["adventure"] == True:
        adventure = Tv_show.query.filter_by(genre="adventure").all()
        for tv_show in adventure:
            tv_shows[tv_show.tv_show_id] = tv_shows
            return jsonify(tv_show_schema.dump(tv_show))
    if preference["science_fiction"] == True:
        science_fiction = Tv_show.query.filter_by(genre="science_fiction").all()
        for tv_show in science_fiction:
            tv_shows[tv_show.tv_show_id] = tv_shows
        return jsonify(tv_show_schema.dump(tv_shows))