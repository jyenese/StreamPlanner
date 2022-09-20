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
    result = movie_schema.dump(movie)
    return jsonify(result)

@movies.route("/", methods=['POST'])
def add_movie():
    movie_fields = movie_schema.load(request.json)
    movie = Movie(
        title = movie_fields['title'],
        genre = movie_fields['genre'],
        date_added = movie_fields['date_added']
    )
    
    db.session.add(movie)
    db.session.commit()
    return jsonify(movie_schema.dump(movie))
