from flask import Blueprint, jsonify
from main import db
from models.movie import Movie
from schemas.movie_schemas import movie_schema, movies_schema

movies = Blueprint('movies',__name__, url_prefix="/movies")

@movies.route("/", methods=['GET'])
def get_movies():
    movies_list = Movie.query.all()
    result = movies_schema.dump(movies_list)
    return jsonify(result)