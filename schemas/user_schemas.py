from main import ma
from marshmallow.validate import Length

class UserSchema(ma.Schema):
    class Meta:
        fields =["user_id","username","email_address","password","dob","country"]
        password = ma.String(validate=Length(min=8))
        
user_schema = UserSchema()
users_schema = UserSchema(many=True)