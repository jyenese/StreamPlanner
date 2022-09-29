from main import ma
from marshmallow import fields
from schemas.movie_schemas import MovieSchema
from schemas.service_schema import ServicesSchema

class MASchema(ma.Schema):
    class Meta:
        ordered = True
        fields =["MA_id","movie_id","movies","service_id","services"]
        load_only = ["movie_id","service_id"]
    movies = fields.Nested(MovieSchema, only=('title',"genre","date_added",))
    services = fields.Nested(ServicesSchema, only=('name',"price"))

ma_schema = MASchema()
mas_schema = MASchema(many=True)
