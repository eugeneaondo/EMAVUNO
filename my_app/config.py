import os
class BaseConfig(object):
    'Base Config class'
    SECRET_KEY = 'A random Secret Key'
    DEBUG=True
    TESTING=False
    NEW_CONFIG_VARIABLE = 'my value'


class ProductionConfig(BaseConfig):
    'Production Specific config'
    DEBUG=False
    SECRET_KEY='Heyo'


class DevelopmentConfig(BaseConfig):
    'Development Specific config'
    DEBUG=True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    'sqlite:///'


    SECRET_KEY='Secret key Development'


config = {
    'development' : DevelopmentConfig,
    'production' : ProductionConfig,
    'default' : DevelopmentConfig
}
    