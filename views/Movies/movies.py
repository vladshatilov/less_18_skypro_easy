import json

from flask import jsonify, request
from flask_restx import Namespace, Resource
from sqlalchemy import desc

from models import Movies, usefull_many, usefull_one
from setup_db import db
from models import Movies, Genres, Directors

movies_ns = Namespace('movies')


@movies_ns.route('/')
class Movies_view(Resource):
    def get(self):
        movies_list = db.session.query(Movies.id, Movies.title, Movies.year,
                                       Movies.description, Movies.trailer,
                                       Movies.genre_id,
                                       Genres.name.label('genre_name'),
                                       Movies.rating,
                                       Movies.director_id
                                       , Directors.name.label('director_name')
                                       ).join(Genres, Movies.genre_id == Genres.id) \
            .join(Directors, Movies.director_id == Directors.id).filter(
            (Movies.year == request.args.get('year') if request.args.get('year') is not None else 1 == 1),
            (Genres.id == request.args.get('genre_id') if request.args.get('genre_id') is not None else 1 == 1),
            (Directors.id == request.args.get('director_id') if request.args.get('director_id') is not None else 1 == 1)
        ).order_by(desc(Movies.year), Movies.title).all()

        return jsonify(usefull_many.dump(movies_list))

    def post(self):
        movie_to_add = request.json
        movie_temp = Movies(**movie_to_add)
        db.session.add(movie_temp)
        db.session.commit()
        return "added", 200


@movies_ns.route('/<int:mid>')
class Movies_view(Resource):
    def get(self, mid):
        movies_list = db.session.query(Movies.id, Movies.title, Movies.year,
                                       Movies.description, Movies.trailer,
                                       Movies.genre_id,
                                       Genres.name.label('genre_name'),
                                       Movies.rating,
                                       Movies.director_id
                                       , Directors.name.label('director_name')
                                       ).join(Genres, Movies.genre_id == Genres.id).join(Directors,
                                                                                         Movies.director_id == Directors.id).filter(
            Movies.id == mid
        ).order_by(desc(Movies.year), Movies.title).all()
        return jsonify(usefull_many.dump(movies_list))

    def put(self,mid):
        movie_to_edit = Movies.query.get(mid)
        movie_details = request.json

        movie_to_edit.title = movie_details.get('title')
        movie_to_edit.description = movie_details.get('description')
        movie_to_edit.trailer = movie_details.get('trailer')
        movie_to_edit.year = movie_details.get('year')
        movie_to_edit.rating = movie_details.get('rating')
        movie_to_edit.genre_id = movie_details.get('genre_id')
        movie_to_edit.director_id = movie_details.get('director_id')

        db.session.add(movie_to_edit)
        db.session.commit()
        return "edited",201

    def delete(self,mid):
        movie_to_delete = Movies.query.get(mid)
        db.session.delete(movie_to_delete)
        db.session.commit()
        return "deleted",204