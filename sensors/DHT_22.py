import __builtin__
import sys
import Adafruit_DHT

class DHT_22(object):
    def __init__(self):
        self.sensor = Adafruit_DHT.DHT22


    def get_pure_read(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, 22)
        return {'humidity': humidity, 'temperature': temperature}