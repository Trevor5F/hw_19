from hw_19.dao.director import DirectorDAO
from hw_19.dao.genre import GenreDAO
from hw_19.dao.movie import MovieDAO
from hw_19.dao.user import UserDAO

from hw_19.service.auth import AuthService
from hw_19.service.user import UserService

from service.director import DirectorService
from service.genre import GenreService
from service.movie import MovieService
from setup_db import db

director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)
user_dao = UserDAO(session=db.session)

director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)
user_service = UserService(dao=user_dao)
auth_service = AuthService(user_service)
