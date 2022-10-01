from main import ma
from marshmallow import fields
from schemas.service_schema import ServicesSchema

class MovieSchema(ma.Schema):
    class Meta:
        ordered = True
        fields =["movie_id", "title","genre","date_added","service","service_id"]
        load_only = ["service_id"]
    service = fields.Nested(ServicesSchema, only=('name',"price","description",))
    
    
        
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)
