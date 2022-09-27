from main import ma

class Services(ma.Schema):
    class Meta:
        fields = ["service_id","name","price","description"]
        
services_schema = Services()