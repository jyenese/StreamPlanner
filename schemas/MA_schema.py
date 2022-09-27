from main import ma

class MASchema(ma.Schema):
    class Meta:
        ordered = True
        fields =["MA_id","name"]
        
ma_schema = MASchema()
mas_schema = MASchema(many=True)
