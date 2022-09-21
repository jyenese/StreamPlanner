from flask import Blueprint, jsonify, request
from main import db
from models.movie import Movie
from schemas.movie_schemas import movie_schema, movies_schema


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

@movies.route("/", methods=['POST'])
def add_movie():
    movie_fields = movie_schema.load(request.json)
    movie = Movie(
        title = movie_fields['title'],
        genre = movie_fields['genre'],
        date_added = movie_fields['date_added'],
        netflix = movie_fields['netflix'],
        disney_plus = movie_fields['disney_plus'],
        stan = movie_fields['stan'],
        binge = movie_fields['binge'],
        appletv = movie_fields['appletv'],
        foxtel = movie_fields['foxtel'],
        amazon_prime = movie_fields['amazon_prime'],
    )
    db.session.add(movie)
    db.session.commit()
    return jsonify(movie_schema.dump(movie))

@movies.route("/<int:id>", methods=['DELETE'])
def delete_movie(id):
    movie = Movie.query.get(id)
    if not movie:
        return {"Error":"Movie ID not found"}
    db.session.delete(movie)
    db.session.commit()    
    return {"message":"Movie has been deleted from the database"}

@movies.route("/<int:id>", methods=['PUT'])
def update_movie(id):
    movie = Movie.query.get(id)
    if not movie:
        return {"Error":"Movie ID not found"}
    
    movie_fields = movie_schema.load(request.json)
    
    movie.title = movie_fields['title']
    movie.genre = movie_fields['genre']
    movie.date_added = movie_fields['date_added']
    movie.netflix = movie_fields['netflix']
    movie.disney_plus = movie_fields['disney_plus']
    movie.stan = movie_fields['stan']
    movie.binge = movie_fields['binge']
    movie.appletv = movie_fields['appletv']
    movie.foxtel = movie_fields['foxtel']
    movie.amazon_prime = movie_fields['amazon_prime']
    
    db.session.commit()
    return jsonify(movie_schema.dump(movie))
    