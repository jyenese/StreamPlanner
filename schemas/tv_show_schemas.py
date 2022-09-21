from main import ma

class Tv_showSchema(ma.Schema):
    class Meta:
        ordered = True
        fields =["tv_show_id", "title","genre","date_added","netflix","disney_plus","stan","binge","appletv","foxtel","amazon_prime"]
        
tv_show_schema = Tv_showSchema()
tv_shows_schema = Tv_showSchema(many=True)