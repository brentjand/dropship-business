from flask import Blueprint, jsonify, abort, request

from ..models import Product, db

bp = Blueprint('products', __name__, url_prefix='/products')


@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    products = Product.query.all() # ORM performs SELECT query
    result = []
    for p in products:
        result.append(p.serialize()) # build list of Accounts as dictionaries
    return jsonify(result) # return JSON response