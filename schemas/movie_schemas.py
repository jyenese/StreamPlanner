from main import ma

class MovieSchema(ma.Schema):
    class Meta:
        ordered = True
        fields =["movie_id", "title","genre","date_added"]
        
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)