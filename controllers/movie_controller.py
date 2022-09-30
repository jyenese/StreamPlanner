from flask import Blueprint, jsonify, request
from main import db
from models.movie import Movie
from schemas.movie_schemas import movie_schema, movies_schema
from models.user import User
from schemas.user_schemas import user_schema
from schemas.preferences_schema import preference_schema, preferences_schema
from models.services import Services
from schemas.service_schema import service_schema, services_schema
from flask_jwt_extended import jwt_required, get_jwt_identity


movies = Blueprint('movies',__name__, url_prefix="/movies")
#The first request, A GET request, shows all of the movies in the database, has request query strings attatched
# for if users want to get fancy and search the route with specific parameters.
@movies.route("/", methods=['GET'])
def get_movies():
    if request.query_string:
        if request.args.get('genre'):
            filtered = Movie.query.filter_by(genre=request.args.get('genre'))
            result = movies_schema.dump(filtered)
            return jsonify(result)
        if request.args.get('title'):
            filtered = Movie.query.filter_by(title=request.args.get('title'))
            result = movies_schema.dump(filtered)
            return jsonify(result)
        if request.args.get('date_added'):
            filtered = Movie.query.filter_by(date_added=request.args.get('date_added'))
            result = movies_schema.dump(filtered)
            return jsonify(result)
        else:
            return {"Error":"You may have typed, genre, title, or date_added wrong."}, 200
    movies_list = Movie.query.all()
    result = movies_schema.dump(movies_list)
    return jsonify(movies_schema.dump(result)),200

@movies.route("/<int:id>", methods=['GET'])
def get_movie(id):
    movie = Movie.query.get(id)
    if not movie:
        return {"error": "Movie ID not found"}
    result = movie_schema.dump(movie)
    return jsonify(result),200

@movies.route("/add", methods=['POST'])
@jwt_required()
def add_movie():
    if get_jwt_identity() != "admin":
        return {"error": "You do not have permission to add"},401
    movie_fields = movie_schema.load(request.json)
    movie = Movie(
        title = movie_fields['title'],
        genre = movie_fields['genre'],
        date_added = movie_fields['date_added'],
        service_id = movie_fields['service_id'],
    )
    db.session.add(movie)
    db.session.commit()
    return jsonify(movie_schema.dump(movie)),201

@movies.route("/delete/<int:id>", methods=['DELETE'])
@jwt_required()
def delete_movie(id):
    if get_jwt_identity() != "admin":
        return {"error": "You do not have permission to delete"}, 401
    movie = Movie.query.get(id)
    if not movie:
        return {"Error":"Movie ID not found"},200
    db.session.delete(movie)
    db.session.commit()    
    return {"message":"Movie has been deleted from the database"},201

@movies.route("/update/<int:id>", methods=['PUT'])
@jwt_required()
def update_movie(id):
    if get_jwt_identity() != "admin":
        return{"error": "You do not have permission to update"}, 401
    movie = Movie.query.get(id)
    if not movie:
        return {"Error":"Movie ID not found"}, 200
    
    movie_fields = movie_schema.load(request.json)
    
    movie.title = movie_fields['title']
    movie.genre = movie_fields['genre']
    movie.date_added = movie_fields['date_added']
    
    db.session.commit()
    return jsonify(movie_schema.dump(movie)),201   


@movies.route("/recommendations", methods=['GET'])
@jwt_required()
def get_movie_recommendations():
    if not get_jwt_identity():
        return {"error": "User not found"}
    user_id = get_jwt_identity() 
    user = User.query.get(user_id)
    movies = {}
    preferences = preferences_schema.dump(user.preferences)
    preference = preferences[0]
    if preference["comedy"] == True:
        comedy = Movie.query.filter_by(genre="comedy").all()
        for movie in comedy:
            movies[movie.movie_id] = movies
            print(movie)    
        return jsonify(movie_schema.dump(movie))

    

    

    

    
