from main import ma
from marshmallow.validate import Length

class AdminSchema(ma.Schema):
    class Meta:
        fields = ('admin_id','username','password','email_address')
        
    password = ma.String(validate=Length(min=8))
    
admin_schema = AdminSchema()