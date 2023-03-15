from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mavuno.db'
db=SQLAlchemy(app)


from my_app.products.views import product
app.register_blueprint(product)

