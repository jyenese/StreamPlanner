from main import ma

class UserSchema(ma.Schema):
    class Meta:
        ordered = True
        fields =["user_id","username","email_address","password","dob","country"]
        
user_schema = UserSchema()
users_schema = UserSchema(many=True)