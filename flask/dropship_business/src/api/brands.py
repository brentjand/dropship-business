from flask import Blueprint, jsonify, abort, request


from ..models import Brand, db


from decimal import Decimal






bp = Blueprint('brands', __name__, url_prefix='/brands')


@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    brands = Brand.query.all() # ORM performs SELECT query
    result = []
    for b in brands:
        result.append(b.serialize()) # build list of Accounts as dictionaries
    return jsonify(result) # return JSON response



@bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def update(id: int):
    b = Brand.query.get_or_404(id)
    if 'address' in request.json:
        b.address = request.json['address']
    if 'email' in request.json:
        b.email = request.json['email']
    if 'name' in request.json:
        b.name = request.json['name']
    db.session.commit()
    return jsonify(b.serialize())



@bp.route('', methods=['POST'])
def create():
    if 'name' not in request.json:
        return abort(400)

    b = Brand(
        address=request.json['address'],
        email=request.json['email'],
        name=request.json['name']
)
    db.session.add(b)
    db.session.commit()

    return jsonify(b.serialize())
