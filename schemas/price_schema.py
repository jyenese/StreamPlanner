from main import ma

class PriceSchema(ma.Schema):
    class Meta:
        ordered = True
        fields =["price_id","netflix","stan","disney_plus","binge","appletv","foxtel","amazon_prime"]
        
price_schema = PriceSchema()
prices_schema = PriceSchema(many=True)
