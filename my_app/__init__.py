from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import config
db=SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    from my_app.auth.views import auth
    app.register_blueprint(auth)

    from my_app.products.views import product
    app.register_blueprint(product)
    
    
    db.init_app(app)

    db.create_all()

    return app

