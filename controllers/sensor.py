from flask_restful import Resource
from flask.json import jsonify
from sensors.DHT_22 import DHT_22

class Sensor(Resource):

    def get(self):
        return jsonify(DHT_22.get_pure_read())