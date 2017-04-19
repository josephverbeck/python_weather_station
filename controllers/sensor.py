import sys
import Adafruit_DHT
from flask_restful import Resource
from flask.json import jsonify
from sensors.DHT_22 import DHT_22

class Sensor(Resource):

    def get(self):
        humitity, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 22)
        temp = int(round(temp)) * 1.8 + 32
        return jsonify({'humitity': humitity, 'temperature': temp})