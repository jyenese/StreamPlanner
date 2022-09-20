from main import ma

class ServiceSchema(ma.Schema):
    class Meta:
        ordered = True
        fields =["service_id", "netflix","disney_plus","stan","binge","appltv","foxtel","amazon_prime"]
        
service_schema = ServiceSchema()
services_schema = ServiceSchema(many=True)