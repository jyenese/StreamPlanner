from operator import truediv
from flask import Blueprint
from main import db
from models.movie import Movie
from models.preferences import Preference
from models.services import Service
from models.tv_show import Tv_show
from models.user import User
from datetime import date

db_commands = Blueprint("db", __name__)

@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print('Tables have been created')
    
@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print('Tables have been dropped')
    
@db_commands.cli.command('seed')
def seed_db():
    movie1 = Movie(
        title = "Intersteller",
        date_added = date(2014,6,11),
        genre = "Adventure, Sci-fi, Drama"
    )
    
    db.session.add(movie1)

    tv_show1 = Tv_show(
        title = "House of the dragon",
        date_added = date(2022,8,20),
        genre = "Action, adventure, drama"
    )
    
    db.session.add(tv_show1)
    
    preference1 = Preference(
        movie = True,
        tv_show = False,
        action = True,
        adventure = True,
        comedy = False,
        fantasy = True,
        horror = False,
        mystery = False,
        drama = True,
        science_fiction = True,
        sport = True
    )
    
    db.session.add(preference1)
    
    services1 = Service(
        netflix = True,
        disney_plus = False,
        stan = True,
        binge = False,
        appletv = True,
        foxtel = True,
        amazon_prime = False
    )
    
    db.session.add(services1)
    
    user1 = User(
        username = "jye",
        email_address = "jye@email.com",
        password = "password",
        dob = date(1995,9,22),
        country = "Australia"
    )
    
    db.session.add(user1)
    
    db.session.commit()
    