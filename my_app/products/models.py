from my_app import db

db.create_all()
class Category(db.Model):

    __name__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer(), primary_key=True)

class Type(db.Model):

    __name__ = 'type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), primary_key=True)
    category_id = db.Column(db.Integer, db.Foreignkey('category.id'))
    category = db.relationship('Category', backref=db.backref('types', lazy='dynamic'))

class Product(db.Model):

    __name__ = 'product'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    alias = db.Column(db.String(50), nullable = True)
    type_id = db.Column(db.Integer, db.ForeignKey('type.id'))
    type = db.relationship('Type', backref=db.backref('products', lazy='dynamic'))



































































































































