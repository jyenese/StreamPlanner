from main import ma

class ServicesSchema(ma.Schema):
    class Meta:
        fields = ["service_id","name","price","description"]
        
services_schema = ServicesSchema()