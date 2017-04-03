from flask_restful import Resource
from flask.json import jsonify


class Version(Resource):

    def get(self):
        return jsonify({'version': "1.0"})
