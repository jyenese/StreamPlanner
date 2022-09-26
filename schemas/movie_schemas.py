from main import ma
from schemas.genre_schema import GenreSchema

class MovieSchema(ma.Schema):
    class Meta:
        ordered = True
        fields =["movie_id", "title","genre""date_added","netflix","disney_plus","stan","binge","appletv","foxtel","amazon_prime"]
        
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)
