from flask import Blueprint,jsonify, request
from main import db
from models.tv_show import Tv_show
from models.user import User
from schemas.tv_show_schemas import tv_show_schema, tv_shows_schema
from schemas.preferences_schema import preferences_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.preferences import all_preferences


tv_shows = Blueprint('tv_shows',__name__, url_prefix="/tv_shows")

#Shows a list of all TV shows.
@tv_shows.route("/", methods=['GET'])
def get_tv_shows():
    if request.query_string:
        if request.args.get('genre'):
            filtered = Tv_show.query.filter_by(genre=request.args.get('genre'))
            result = tv_shows_schema.dump(filtered)
            if len(result) == 0:
                return {"Error":"Your search returned zero results"},404
            return jsonify(result)
        if request.args.get('title'):
            filtered = Tv_show.query.filter_by(title=request.args.get('title'))
            result = tv_shows_schema.dump(filtered)
            if len(result) == 0:
                return {"Error":"Your search returned zero results"},404
            return jsonify(result)
        if request.args.get('date_added'):
            filtered = Tv_show.query.filter_by(date_added=request.args.get('date_added'))
            result = tv_shows_schema.dump(filtered)
            if len(result) == 0:
                return {"Error":"Your search returned zero results"},404
            return jsonify(result)
        else:
            return {"Error":"You may have typed, genre, title, or date_added wrong."},200
    tv_shows = Tv_show.query.all()
    result = tv_shows_schema.dump(tv_shows)
    return jsonify(result), 200

#Search the database for a certain TV_show_id (title), and if there isnt one, give an error.
@tv_shows.route("/<int:id>", methods=['GET'])
def get_tv_show(id):
    tv_shows = Tv_show.query.get(id)
    if not tv_shows:
        return {"error": "tv_show not found"},404
    result = tv_show_schema.dump(tv_shows)
    return jsonify(result), 200

#Asking for Admin ID, then if given, you have access to add to the database a 'TV show'
@tv_shows.route("/", methods=['POST'])
@jwt_required()
def add_tv_show():
    if get_jwt_identity() != "admin":
        return {"error": "You do not have permission to add"}, 401
    tv_show_fields = tv_show_schema.load(request.json)
    tv_show = Tv_show(
        title = tv_show_fields['title'],
        genre = tv_show_fields['genre'],
        date_added = tv_show_fields['date_added'],
        service_id = tv_show_fields['service_id'],
    )
    db.session.add(tv_show)
    db.session.commit()
    return jsonify(tv_show_schema.dump(tv_show)),201

#Asking for Admin ID, then if given, you have access to delete the TV show
@tv_shows.route("/<int:id>", methods=['DELETE'])
@jwt_required()
def delete_tv_show(id):
    if get_jwt_identity() != "admin":
        return {"error": "You do not have permission to delete"}, 401
    tv_show = Tv_show.query.get(id)
    if not tv_show:
        return {"Error":"Tv_show ID not found"},404
    
    db.session.delete(tv_show)
    db.session.commit() 
    return {"message":"TV Show removed"},201

#Asking for Admin ID, then if given, you have access to update the TV show
@tv_shows.route("/<int:id>", methods=['PUT'])
@jwt_required()
def update_tv_show(id):
    if get_jwt_identity() != "admin":
        return {"error": "You do not have permission to update"}, 401
    tv_show = Tv_show.query.get(id)
    if not tv_show:
        return {"Error":"TV Show ID not found"},200
    
    tv_show_fields = tv_show_schema.load(request.json)
    
    tv_show.title = tv_show_fields['title']
    tv_show.genre = tv_show_fields['genre']
    tv_show.date_added = tv_show_fields['date_added']
    tv_show.service_id = tv_show_fields['service_id']
    
    db.session.commit()
    return jsonify(tv_show_schema.dump(tv_show)),201

#Showing an example of how it would work, The ID of TV show with the service its on
@tv_shows.route("/recommendations", methods=['GET'])
@jwt_required()
def get_tv_recommendations():
    if not get_jwt_identity():
        return {"error": "User not found"},401
    # Get the user preferences of what genre they are interested in
    user_id = get_jwt_identity() 
    user = User.query.get(user_id)
    user_preferences = preferences_schema.dump(user.preferences)
    user_preference = user_preferences[0]
    # Find movies that the user is interested in via the preference and movie genres
    tv_shows = []
    for preference in all_preferences:   
        if user_preference[preference] == True:
            results = Tv_show.query.filter_by(genre=preference).all()
            for tv_show in results:
                tv_shows.append(tv_show_schema.dump(tv_show))
    # Find the recommended service by counting movies by service name           
    recommended_service = ""
    service_count = {}
    for tv_show in tv_shows:
        service_name = tv_show["service"]["name"]
        if not service_name in service_count:
            service_count[service_name] = 0
        service_count[service_name] += 1
    
    highest_count = -1
    for service, count in service_count.items():
        if count > highest_count:
            recommended_service = service
            highest_count = count     
    # Build the response
    response = {
        "recommendations": tv_shows,
        "recommended_service": recommended_service,       
    }        
    
    return jsonify(response)