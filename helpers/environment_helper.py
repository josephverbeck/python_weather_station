import __builtin__
import os
import yaml

class EnvironmentHelper(object):

    @staticmethod
    def set_environment():
        __builtin__.environemnt = os.environ['ENVIRONMENT']
        with open(os.path.abspath("config/environment.yml"), 'r') as yaml_file:
            __builtin__.config_environment = yaml.load(yaml_file)
