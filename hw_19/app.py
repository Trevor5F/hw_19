from flask import Flask
from flask_restx import Api

from hw_19.config import Config
from hw_19.dao.model.user import User
from hw_19.setup_db import db
from hw_19.views.auth import auth_ns
from hw_19.views.directors import director_ns
from hw_19.views.genres import genre_ns
from hw_19.views.movies import movie_ns
from hw_19.views.users import user_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    app.config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 3}
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
