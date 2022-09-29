from main import ma
from marshmallow import fields
from schemas.tv_show_schemas import Tv_showSchema
from schemas.service_schema import ServicesSchema

class TVASchema(ma.Schema):
    class Meta:
        ordered = True
        fields =["TVA_id","tv_show_id","tv_show","service_id","services"]
        load_only = ["tv_show_id","service_id"]
    tv_show = fields.Nested(Tv_showSchema, only=('title',"genre","date_added",))
    services = fields.Nested(ServicesSchema, only=('name',"price"))
        
tva_schema = TVASchema()
tvas_schema = TVASchema(many=True)
