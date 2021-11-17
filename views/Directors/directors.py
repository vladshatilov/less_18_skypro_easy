from flask import jsonify
from flask_restx import Namespace, Resource
from models import Directors, usefull_many, usefull_one

directors_ns = Namespace('directors')

@directors_ns.route('/')
class Directors_view(Resource):
    def get(self):
        directors_list = Directors.query.all()
        return jsonify(usefull_many.dump(directors_list))

@directors_ns.route('/<int:did>')
class Directors_view(Resource):
    def get(self,did):
        director_one = Directors.query.get(did)
        return jsonify(usefull_one.dump(director_one))