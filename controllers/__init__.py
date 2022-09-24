from controllers.movie_controller import movies
from controllers.preferences_controller import preferences
from controllers.tv_show_controller import tv_shows
from controllers.auth_controller import auth
from controllers.price_controller import price

registerable_controllers = [movies, preferences,price,tv_shows, auth]