from main import ma
from schemas.genre_schema import GenreSchema

class Tv_showSchema(ma.Schema):
    class Meta:
        ordered = True
        fields =["tv_show_id", "title",GenreSchema,"date_added","netflix","disney_plus","stan","binge","appletv","foxtel","amazon_prime"]
        
tv_show_schema = Tv_showSchema()
tv_shows_schema = Tv_showSchema(many=True)