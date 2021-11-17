from flask import jsonify
from flask_restx import Namespace, Resource
from models import Genres, usefull_many, usefull_one

genres_ns = Namespace('genres')

@genres_ns.route('/')
class Genres_view(Resource):
    def get(self):
        genres_list = Genres.query.all()
        return jsonify(usefull_many.dump(genres_list))

@genres_ns.route('/<int:gid>')
class Genres_view(Resource):
    def get(self,gid):
        genres_one = Genres.query.get(gid)
        return jsonify(usefull_one.dump(genres_one))