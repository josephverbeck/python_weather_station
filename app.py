import logging

import flask
import flask_cors
import flask_restful
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

from helpers.environment_helper import EnvironmentHelper
from controllers.version import Version
from controllers.sensor import Sensor


app = flask.Flask(__name__)
api = flask_restful.Api(app)
# Very important for development as this stands for Cross Origin Resource sharing. Essentially this is what allows for
# the UI to be run on the same box as this middleware piece of code. Consider this code boiler plate.
cors = flask_cors.CORS(app, resources={r"/api/*": {"origins": "*"}})


EnvironmentHelper.set_environment()

api.add_resource(Version, '/api/v1/version')

api.add_resource(Sensor, '/api/v1/pure_read')

if __name__ == '__main__':
    print "starting server on port 21405"
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(port=21405)
    IOLoop.instance().start()