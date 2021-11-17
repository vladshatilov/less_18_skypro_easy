# здесь модель SQLAlchemy для сущности, также могут быть дополнительные методы работы с моделью (но не с базой)

# Пример
from marshmallow import Schema, fields
from sqlalchemy.orm import relationship

from setup_db import db



class Movies(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))
    genre = db.relationship('Genres')
    director = db.relationship('Directors')


class Genres(db.Model):
    __tablename__ = 'genre'
    # id = db.Column(db.Integer, db.ForeignKey('movies.genre_id'), primary_key=True)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class Directors(db.Model):
    __tablename__ = 'director'
    # id = db.Column(db.Integer, db.ForeignKey('movies.director_id'), primary_key=True)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

class Usefull_scheme(Schema):
    id = fields.Int()
    title = fields.String()
    description = fields.String()
    trailer = fields.String()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()
    genre_name = fields.String()
    director_name = fields.String()
    name = fields.String()

usefull_one = Usefull_scheme()
usefull_many = Usefull_scheme(many=True)