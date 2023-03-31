
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    'Base Config class'
    SECRET_KEY = 'A random Secret Key'
    DEBUG=True
    TESTING=False
    NEW_CONFIG_VARIABLE = 'my value'

    @staticmethod
    def init_app(app):
        pass

class ProductionConfig(BaseConfig):
    'Production Specific config'
    DEBUG=False
    SECRET_KEY='Heyo'


class DevelopmentConfig(BaseConfig):
    'Development Specific config'
    DEBUG=True
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'emavuno.sqlite')


    SECRET_KEY='Secret key Development'


config = {
    'development' : DevelopmentConfig,
    'production' : ProductionConfig,
    'default' : DevelopmentConfig
}
    