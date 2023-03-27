from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mavuno.db'

    from my_app.products.views import product
    app.register_blueprint(product)
    
    with app.app_context():
        db.init_app(app)

    return app




db.create_all()
