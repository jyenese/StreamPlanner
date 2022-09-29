from operator import truediv
from flask import Blueprint
from main import db
from main import bcrypt
from models.movie import Movie
from models.preferences import Preference
from models.tv_show import Tv_show
from models.admin import Admin
from models.services import Services
from datetime import date
from models.MA import MA
from models.TVA import TVA
from models.user import User

db_commands = Blueprint("db", __name__)

@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print('Tables have been created')

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print('tables have been dropped')
    
    
@db_commands.cli.command('seed')
def seed_db():
    service1 = Services(
        name = "Netflix",
        price = 10.99,
        description = "Worldwide streaming service."
    )
    
    db.session.add(service1)
    db.session.commit()
    
    service2 = Services(
        name = "Binge",
        price = 14.99,
        description = "Australian streaming service."
    )
    
    db.session.add(service2)
    db.session.commit()
    
    movie1 = Movie(
        title = "Intersteller",
        date_added = date(2014,6,11),
        genre = "science_fiction"
        
    )
    
    db.session.add(movie1)
    db.session.commit()
    
    movie2 = Movie(
        title = "The Martian",
        date_added = date(2017,8,11),
        genre = "mystery"
        
    )
    
    db.session.add(movie2)
    db.session.commit()
    
    movie3 = Movie(
        title = "Intersteller: Reborn",
        date_added = date(2024,6,11),
        genre = "comedy"
        
    )
    
    db.session.add(movie3)
    db.session.commit()
    
    tv1 = Tv_show(
        title = "True Blood",
        date_added = date(2011,4,11),
        genre = "science_fiction"
        
    )
    
    db.session.add(tv1)
    db.session.commit()
    
    tv2 = Tv_show(
        title = "House of the Dragon",
        date_added = date(2022,8,3),
        genre = "adventure"
        
    )
    
    db.session.add(tv2)
    db.session.commit()
    
    
    movie_available1 = MA(
        movie_id = movie1.movie_id,
        service_id = service1.service_id
        
    )
    db.session.add(movie_available1)
    db.session.commit()
    
    tv_available1 = TVA(
        tv_show_id = tv1.tv_show_id,
        service_id = service2.service_id
        
    )
    db.session.add(tv_available1)
    db.session.commit()
    
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
    db.session.commit()
    
    preference1 = Preference(
        action = True,
        adventure = True,
        comedy = True,
        fantasy = True,
        horror = True,
        mystery = False,
        drama = True,
        science_fiction = True,
        user_id = user1.user_id
    )
    
    db.session.add(preference1)
    db.session.commit()
    print("Seeded")
    
