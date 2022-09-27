from main import ma

class TVASchema(ma.Schema):
    class Meta:
        ordered = True
        fields =["TVA_id","name"]
        
tva_schema = TVASchema()
tvas_schema = TVASchema(many=True)
