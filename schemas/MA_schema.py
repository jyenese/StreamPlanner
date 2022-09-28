from main import ma
from marshmallow import fields
from schemas.movie_schemas import MovieSchema
from schemas.service_schema import ServicesSchema

class MASchema(ma.Schema):
    class Meta:
        ordered = True
        fields =["MA_id","movie_id","service_id"]
    #     load_only = ["movie_id","service_id"]
    # movie = fields.Nested(MovieSchema, only=('genre',))

ma_schema = MASchema()
mas_schema = MASchema(many=True)
