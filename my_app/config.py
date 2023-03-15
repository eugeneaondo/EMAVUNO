class BaseConfig(object):
    'Base Config class'
    SECRET_KEY = 'A random Secret Key'
    DEBUG=True
    TESTING=False
    NEW_CONFIG_VARIABLE = 'my value'


class ProductionConfig(BaseConfig):
    'Production Specific config'
    DEBUG=False
    SECRET_KEY=open('/path/to/secret/file').read()


class DevelopmentConfig(BaseConfig):
    'Development Specific config'
    DEBUG=True
    TESTING = True


    SECRET_KEY='Secret key Development'

    