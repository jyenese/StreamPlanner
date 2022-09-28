from main import ma

class TVASchema(ma.Schema):
    class Meta:
        ordered = True
        fields =["TVA_id","tv_show_id","service_id"]
        
tva_schema = TVASchema()
tvas_schema = TVASchema(many=True)
