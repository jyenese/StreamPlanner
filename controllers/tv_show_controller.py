from flask import Blueprint,jsonify
from main import db
from models.tv_show import Tv_show
from schemas.tv_show_schemas import tv_show_schema, tv_shows_schema

tv_shows = Blueprint('tv_shows',__name__, url_prefix="/tv_show")

@tv_shows.route("/", methods=['GET'])
def get_tv_shows():
    tv_shows = Tv_show.query.all()
    result = tv_shows_schema.dump(tv_shows)
    return jsonify(result)