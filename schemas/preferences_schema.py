from main import ma
from marshmallow import fields
from schemas.user_schemas import UserSchema

class PreferenceSchema(ma.Schema):
    class Meta:
        ordered = True
        fields =["preference_id","user_id","user","action","adventure", "comedy"
                 ,"fantasy","horror","mystery","drama","science_fiction"]
        
        load_only = ['user_id']
    user = fields.Nested(UserSchema, only=("username",))
    
preference_schema = PreferenceSchema()
preferences_schema = PreferenceSchema(many=True)