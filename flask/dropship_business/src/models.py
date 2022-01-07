from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

db = SQLAlchemy()




# Reference:
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
# https://docs.sqlalchemy.org/en/14/core/metadata.html#sqlalchemy.schema.Column
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#many-to-many-relationships


class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(75), nullable=False)


    def __init__(self, name: str, email: str, address: str):
        self.name = name
        self.email = email
        self.address = address

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'address': self.address
        }

class Account(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    purpose = db.Column(db.String(50), nullable=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    customer = db.relationship("Customer", uselist=False)

    def __init__(self, username: str, purpose: str):
        self.username = username
        self.purpose = purpose

    def serialize(self):
        return {
            'id': self.id,
            'name': self.username,
            'purpose': self.purpose
    }

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_quantity = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'), nullable=False)


    def __init__(self, product_quantity: str, product_id: str, account_id: str, brand_id: str):
        self.product_quantity = product_quantity
        self.product_id = product_id
        self.brand_id = brand_id
        self.account_id = account_id

    def serialize(self):
        return {
            'id': self.id,
            'product_quantity': self.product_quantity,
            'product_id': self.product_id,
            'brand_id': self.brand_id,
            'account_id': self.account_id
        }


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(30), unique=True, nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'), nullable=False)


    def __init__(self, description: str):
        self.description = description

    def serialize(self):
        return {
            'id':self.id,
            'description':self.description
        }


class Brand(db.Model):
    __tablename__ = 'brands'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(100), nullable=False)
    distributors = db.relationship('Distributor', backref='brand', cascade="all,delete")

    def __init__(self, name: str, email: str, address: str):
        self.name = name
        self.email = email
        self.address = address

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'address': self.address
        }

brand_distribution = db.Table('brand_distribution', 
    db.Column('brand_id', db.Integer,db.ForeignKey('brands.id'), primary_key=True),
    db.Column('distributor_id', db.Integer,db.ForeignKey('distributors.id'), primary_key=True)
)

class Distributor(db.Model):
    __tablename__ = 'distributors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(75), nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'), nullable=False)
    contracts = db.relationship('Brand', secondary=brand_distribution, lazy='subquery', backref=db.backref('brand_contracts', lazy=True))

class Parcel(db.Model):
    __tablename__ = 'parcels'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usps_tracking_number = db.Column(db.Integer(), unique=True, nullable=False)
    shipment_date = db.Column(db.String(10), nullable=False)
    estimated_delivery_date = db.Column(db.DateTime(20), nullable=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    distributor_id = db.Column(db.Integer, db.ForeignKey('distributors.id'), nullable=False)

    def __init__(self, usps_tracking_number: str, shipment_date: str, estimated_delivery_date: str, 
    customer_id: str, distributor_id: str):
         self.shipment_date = shipment_date
         self.estimated_delivery_date = estimated_delivery_date
         self.customer_id = customer_id
         self.distributor_id = distributor_id
        

    def serialize(self):
        return {
            'id': self.id,
            'shipment_date': self.shipment_date,
            'estimated_delivery_date': self.estimated_delivery_date,
            'customer_id': self.customer_id,
            'distributor_id': self.distributor_id
        }
