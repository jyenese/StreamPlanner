from flask import Blueprint, jsonify, request
from main import db
from models.movie import Movie
from models.MA import MA
from schemas.movie_schemas import movie_schema, movies_schema
from schemas.MA_schema import ma_schema, mas_schema
from flask_jwt_extended import jwt_required, get_jwt_identity


movies = Blueprint('movies',__name__, url_prefix="/movies")

@movies.route("/", methods=['GET'])
def get_movies():
    movies_list = Movie.query.all()
    result = movies_schema.dump(movies_list)
    return jsonify(result)

@movies.route("/<int:id>", methods=['GET'])
def get_movie(id):
    movie = Movie.query.get(id)
    if not movie:
        return {"error": "Movie ID not found"}
    result = movie_schema.dump(movie)
    return jsonify(result)

@movies.route("/add", methods=['POST'])
@jwt_required()
def add_movie():
    if get_jwt_identity() != "admin":
        return {"error": "You do not have permission to add"}
    movie_fields = movie_schema.load(request.json)
    movie = Movie(
        title = movie_fields['title'],
        genre = movie_fields['genre'],
        date_added = movie_fields['date_added'],
    )
    db.session.add(movie)
    db.session.commit()
    return jsonify(movie_schema.dump(movie))

@movies.route("/<int:id>", methods=['DELETE'])
@jwt_required()
def delete_movie(id):
    if get_jwt_identity() != "admin":
        return {"error": "You do not have permission to delete"}
    movie = Movie.query.get(id)
    if not movie:
        return {"Error":"Movie ID not found"}
    db.session.delete(movie)
    db.session.commit()    
    return {"message":"Movie has been deleted from the database"}

@movies.route("/<int:id>", methods=['PUT'])
@jwt_required()
def update_movie(id):
    if get_jwt_identity() != "admin":
        return{"error": "You do not have permission to update"}
    movie = Movie.query.get(id)
    if not movie:
        return {"Error":"Movie ID not found"}
    
    movie_fields = movie_schema.load(request.json)
    
    movie.title = movie_fields['title']
    movie.genre = movie_fields['genre']
    movie.date_added = movie_fields['date_added']
    
    db.session.commit()
    return jsonify(movie_schema.dump(movie))
    
# @movies.route("/available", methods=['GET'])
# def movies_available():
#     movies_list = MA.query.all()
#     result = ma_schema.dump(movies_list)
#     db.session.commit()
#     return (jsonify(result))

@movies.route("/available", methods=['GET'])
def get_movies_available():
    movies_list = MA.query.all()
    result = mas_schema.dump(movies_list)
    return jsonify(result)
    

    
