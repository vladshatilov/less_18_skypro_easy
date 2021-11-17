# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение

# Пример

from flask import Flask
from flask_restx import Api
#
from config import Config
from models import Movies,Directors,Genres
from setup_db import db
from views.Directors.directors import directors_ns
from views.Genres.genres import genres_ns
from views.Movies.movies import movies_ns
# from views.books import book_ns
# from views.reviews import review_ns
#
# функция создания основного объекта app
def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app
#
#
# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(movies_ns)
    # create_data(app, db)
#
#
# функция
def create_data(app, db):
    with app.app_context():
        db.create_all()
        # a1 = Book(id ='Mdk',name = 'Mdk',author = 'Mdk',year = 'Mdk')
        # with db.session.begin():
        #     db.session.add_all([a1,a2])
#
#
app = create_app(Config())
app.debug = True
#
if __name__ == '__main__':
    # app.run(host="localhost", port=10001, debug=True)
    app.run(host="localhost", debug=True)



