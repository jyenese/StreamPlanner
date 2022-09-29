from main import ma

class ServicesSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["service_id","name","price","description"]
service_schema = ServicesSchema()        
services_schema = ServicesSchema(many=True)