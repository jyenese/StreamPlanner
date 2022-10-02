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
    netflix = Services(
        name = "Netflix",
        price = 10.99,
        description = "Worldwide streaming service."
    )
    
    db.session.add(netflix)
    db.session.commit()
    
    binge = Services(
        name = "Binge",
        price = 14.99,
        description = "Australian streaming service."
    )
    
    db.session.add(binge)
    db.session.commit()
    
    stan = Services(
        name = "Stan",
        price = 9.99,
        description = "Australian streaming service."
    )
    
    db.session.add(stan)
    db.session.commit()
    
    amazon_prime = Services(
        name = "Amazon Prime",
        price = 11.99,
        description = "Worldwide streaming service."
    )
    
    db.session.add(amazon_prime)
    db.session.commit()
    
    Disney_plus= Services(
        name = "Disney Plus",
        price = 8.99,
        description = "Worldwide streaming service."
    )
    
    db.session.add(Disney_plus)
    db.session.commit()
    
    AppleTV = Services(
        name = "Apple TV",
        price = 14.99,
        description = "Worldwide streaming service."
    )
    
    db.session.add(AppleTV)
    db.session.commit()
    

    
    db.session.add(Movie(
        title = "Intersteller",
        date_added = date(2014,6,11),
        genre = "science_fiction",
        service_id = netflix.service_id))
    
    
    db.session.add(Movie(
        title = "The Martian",
        date_added = date(2017,8,11),
        genre = "science_fiction",
        service_id = netflix.service_id   
    ))
    
    db.session.add(Movie(
        title = "Intersteller: Reborn",
        date_added = date(2024,6,11),
        genre = "science_fiction",
        service_id = netflix.service_id        
    ))
    
    db.session.add(Movie(
        title = "Mean Girls",
        date_added = date(2007,6,11),
        genre = "Drama",
        service_id = netflix.service_id,        
    ))
    
    db.session.add(Movie(
        title = "The GodFather",
        date_added = date(1972,6,1),
        genre = "Drama",
        service_id = binge.service_id,        
    ))
    
    db.session.add(Movie(
        title = "The Shawshank Redemption",
        date_added = date(1994,3,11),
        genre = "Drama",
        service_id = binge.service_id,        
    ))
    
    db.session.add(Movie(
        title = "Die Hard",
        date_added = date(1988,3,21),
        genre = "action",
        service_id = binge.service_id,        
    ))
    
    db.session.add(Movie(
        title = "Mad Max 2: The Road Warrior",
        date_added = date(1981,2,11),
        genre = "action",
        service_id = binge.service_id,        
    ))
    db.session.add(Movie(
        title = "Terminator 2: Judgement Day",
        date_added = date(1991,1,1),
        genre = "action",
        service_id = stan.service_id,        
    ))
    db.session.add(Movie(
        title = "Thor: Love and Thunder",
        date_added = date(2022,3,21),
        genre = "adventure",
        service_id = stan.service_id,        
    ))
    db.session.add(Movie(
        title = "Avatar: The Way of Water",
        date_added = date(2022,8,11),
        genre = "adventure",
        service_id = stan.service_id,        
    ))
    db.session.add(Movie(
        title = "Lord of the Rings: The Fellowship of the Ring",
        date_added = date(2001,2,11),
        genre = "adventure",
        service_id = stan.service_id,        
    ))
    db.session.add(Movie(
        title = "Step Brothers",
        date_added = date(2008,2,11),
        genre = "comedy",
        service_id = amazon_prime.service_id,        
    ))
    db.session.add(Movie(
        title = "SuperBad",
        date_added = date(2007,6,11),
        genre = "comedy",
        service_id = amazon_prime.service_id,        
    ))
    db.session.add(Movie(
        title = "Dumb and Dumber",
        date_added = date(1994,1,11),
        genre = "comedy",
        service_id = amazon_prime.service_id,        
    ))
    db.session.add(Movie(
        title = "The Hobbit: An Unexpected Journey",
        date_added = date(2012,3,14),
        genre = "fantasy",
        service_id = amazon_prime.service_id,        
    ))
    db.session.add(Movie(
        title = "Peter Pan",
        date_added = date(2002,2,11),
        genre = "fantasy",
        service_id = Disney_plus.service_id,        
    ))
    db.session.add(Movie(
        title = "Pinocchio",
        date_added = date(2019,1,11),
        genre = "fantasy",
        service_id = Disney_plus.service_id,        
    ))
    db.session.add(Movie(
        title = "Saw: Original",
        date_added = date(2004,2,11),
        genre = "horror",
        service_id = Disney_plus.service_id,        
    ))
    db.session.add(Movie(
        title = "Hellraiser",
        date_added = date(1987,2,11),
        genre = "horror",
        service_id = Disney_plus.service_id,        
    ))
    db.session.add(Movie(
        title = "Kill List",
        date_added = date(2009,2,11),
        genre = "horror",
        service_id = AppleTV.service_id,        
    ))
    db.session.add(Movie(
        title = "Saw: Original",
        date_added = date(2004,2,11),
        genre = "horror",
        service_id = AppleTV.service_id,        
    ))
    db.session.add(Movie(
        title = "The Girl with The Dragon Tattoo",
        date_added = date(2011,1,13),
        genre = "mystery",
        service_id = AppleTV.service_id,        
    ))
    db.session.add(Movie(
        title = "Kiss the Girls",
        date_added = date(1997,4,13),
        genre = "mystery",
        service_id = stan.service_id,        
    ))
    db.session.add(Movie(
        title = "Get Out",
        date_added = date(2001,1,13),
        genre = "mystery",
        service_id = netflix.service_id,        
    ))
    
    
    db.session.add(Tv_show(
        title = "Intersteller",
        date_added = date(2014,6,11),
        genre = "science_fiction",
        service_id = netflix.service_id))
    
    
    db.session.add(Tv_show(
        title = "The Martian",
        date_added = date(2017,8,11),
        genre = "science_fiction",
        service_id = netflix.service_id   
    ))
    
    db.session.add(Tv_show(
        title = "Intersteller: Reborn",
        date_added = date(2024,6,11),
        genre = "science_fiction",
        service_id = netflix.service_id        
    ))
    
    db.session.add(Tv_show(
        title = "Mean Girls",
        date_added = date(2007,6,11),
        genre = "Drama",
        service_id = netflix.service_id,        
    ))
    
    db.session.add(Tv_show(
        title = "The GodFather",
        date_added = date(1972,6,1),
        genre = "Drama",
        service_id = binge.service_id,        
    ))
    
    db.session.add(Tv_show(
        title = "The Shawshank Redemption",
        date_added = date(1994,3,11),
        genre = "Drama",
        service_id = binge.service_id,        
    ))
    
    db.session.add(Tv_show(
        title = "Die Hard",
        date_added = date(1988,3,21),
        genre = "action",
        service_id = binge.service_id,        
    ))
    
    db.session.add(Tv_show(
        title = "Mad Max 2: The Road Warrior",
        date_added = date(1981,2,11),
        genre = "action",
        service_id = binge.service_id,        
    ))
    db.session.add(Tv_show(
        title = "Terminator 2: Judgement Day",
        date_added = date(1991,1,1),
        genre = "action",
        service_id = stan.service_id,        
    ))
    db.session.add(Tv_show(
        title = "Thor: Love and Thunder",
        date_added = date(2022,3,21),
        genre = "adventure",
        service_id = stan.service_id,        
    ))
    db.session.add(Tv_show(
        title = "Avatar: The Way of Water",
        date_added = date(2022,8,11),
        genre = "adventure",
        service_id = stan.service_id,        
    ))
    db.session.add(Tv_show(
        title = "Lord of the Rings: The Fellowship of the Ring",
        date_added = date(2001,2,11),
        genre = "adventure",
        service_id = stan.service_id,        
    ))
    db.session.add(Tv_show(
        title = "Step Brothers",
        date_added = date(2008,2,11),
        genre = "comedy",
        service_id = amazon_prime.service_id,        
    ))
    db.session.add(Tv_show(
        title = "SuperBad",
        date_added = date(2007,6,11),
        genre = "comedy",
        service_id = amazon_prime.service_id,        
    ))
    db.session.add(Tv_show(
        title = "Dumb and Dumber",
        date_added = date(1994,1,11),
        genre = "comedy",
        service_id = amazon_prime.service_id,        
    ))
    db.session.add(Tv_show(
        title = "The Hobbit: An Unexpected Journey",
        date_added = date(2012,3,14),
        genre = "fantasy",
        service_id = amazon_prime.service_id,        
    ))
    db.session.add(Tv_show(
        title = "Peter Pan",
        date_added = date(2002,2,11),
        genre = "fantasy",
        service_id = Disney_plus.service_id,        
    ))
    db.session.add(Tv_show(
        title = "Pinocchio",
        date_added = date(2019,1,11),
        genre = "fantasy",
        service_id = Disney_plus.service_id,        
    ))
    db.session.add(Tv_show(
        title = "Saw: Original",
        date_added = date(2004,2,11),
        genre = "horror",
        service_id = Disney_plus.service_id,        
    ))
    db.session.add(Tv_show(
        title = "Hellraiser",
        date_added = date(1987,2,11),
        genre = "horror",
        service_id = Disney_plus.service_id,        
    ))
    db.session.add(Tv_show(
        title = "Kill List",
        date_added = date(2009,2,11),
        genre = "horror",
        service_id = AppleTV.service_id,        
    ))
    db.session.add(Tv_show(
        title = "Saw: Original",
        date_added = date(2004,2,11),
        genre = "horror",
        service_id = AppleTV.service_id,        
    ))
    db.session.add(Tv_show(
        title = "The Girl with The Dragon Tattoo",
        date_added = date(2011,1,13),
        genre = "mystery",
        service_id = AppleTV.service_id,        
    ))
    db.session.add(Tv_show(
        title = "Kiss the Girls",
        date_added = date(1997,4,13),
        genre = "mystery",
        service_id = stan.service_id,        
    ))
    db.session.add(Tv_show(
        title = "Get Out",
        date_added = date(2001,1,13),
        genre = "mystery",
        service_id = netflix.service_id,        
    ))
    
    
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
        mystery = True,
        drama = True,
        science_fiction = True,
        user_id = user1.user_id
    )
    
    db.session.add(preference1)
    db.session.commit()
    print("Seeded")
    
