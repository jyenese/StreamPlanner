from main import ma

class PreferenceSchema(ma.Schema):
    class Meta:
        ordered = True
        fields =["preference_id","movie","tv_show", "action","adventure", "comedy","fantasy","horror","mystery","drama","science_fiction"]
        
preference_schema = PreferenceSchema()
preferences_schema = PreferenceSchema(many=True)