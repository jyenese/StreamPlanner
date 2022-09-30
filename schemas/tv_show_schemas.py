from main import ma
from marshmallow import fields
from schemas.service_schema import ServicesSchema

class Tv_showSchema(ma.Schema):
    class Meta:
        ordered = True
        fields =["tv_show_id", "title","genre","date_added","service_id","services",]
        load_only = ["service_id"]
    services = fields.Nested(ServicesSchema, only=('name',"price","description",))
        
tv_show_schema = Tv_showSchema()
tv_shows_schema = Tv_showSchema(many=True)