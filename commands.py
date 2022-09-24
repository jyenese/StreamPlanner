from operator import truediv
from flask import Blueprint
from main import db
from main import bcrypt
from models.movie import Movie
from models.preferences import Preference
from models.tv_show import Tv_show
from models.user import User
from models.price import Price 
from models.admin import Admin
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
        genre = "Adventure,Science-fiction,Drama",
        netflix = True,
        disney_plus = False,
        stan = True,
        binge = False,
        appletv = True,
        foxtel = True,
        amazon_prime = False
    )
    
    db.session.add(movie1)

    tv_show1 = Tv_show(
        title = "House of the dragon",
        date_added = date(2022,8,20),
        genre = "Action, adventure, drama",
        netflix = True,
        disney_plus = False,
        stan = True,
        binge = False,
        appletv = True,
        foxtel = True,
        amazon_prime = False
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
    
    admin1 = Admin(
        username = "admin",
        password = bcrypt.generate_password_hash("password2").decode("utf-8"),
        email_address = "admin@example.com",
    )
    db.session.add(admin1)
    
    user1 = User(
        username = "jye",
        email_address = "jye@email.com",
        password = bcrypt.generate_password_hash("password").decode("utf-8"),
        dob = date(1995,9,22),
        country = "Australia"
    )
    db.session.add(user1)
    
    user2 = User(
        username = "sam",
        email_address = "sam@email.com",
        password = bcrypt.generate_password_hash("password").decode("utf-8"),
        dob = date(1993,10,11),
        country = "New Zealand"
    )
    db.session.add(user2)
    
    user3 = User(
        username = "taya",
        email_address = "taya@email.com",
        password = bcrypt.generate_password_hash("password").decode("utf-8"),
        dob = date(1997,12,22),
        country = "France"
    )
    db.session.add(user3)
    
    user4 = User(
        username = "Tony",
        email_address = "Tony@email.com",
        password = bcrypt.generate_password_hash("password").decode("utf-8"),
        dob = date(1966,6,28),
        country = "Indonesia"
    )
    db.session.add(user4)
    
    price1 = Price(
        netflix = 10.99,
        stan = 11.99,
        disney_plus = 12.99,
        binge = 9.99,
        apple_tv = 10.99,
        foxtel = 30.99,
        amazon_prime = 8.99,
        date = "2022-9-9"
        
    )
    db.session.add(price1)
    
    db.session.commit()
    