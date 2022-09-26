from main import ma

class GenreSchema(ma.Schema):
    class Meta:
        fields = ('movie','tv show','action','adventure','comedy','horror', 'mystery', 'drama', 'science fiction', 'sport')
genre_schema = GenreSchema()

class List():
    movie = "movie"
    tv_show = "tv show"
    action = "action"
    drama = "drama"
    adventure = "adventure"
    comedy = "comedy"
    horror = "horror"
    mystery = "mystery"
    science_fiction = "science_fiction"
    sport = "sport"