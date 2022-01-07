from flask import Blueprint, jsonify, abort, request
jsonify
from ..models import Account, db
import hashlib
import secrets


def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()

bp = Blueprint('accounts', __name__, url_prefix='/accounts')


@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    accounts = Account.query.all() # ORM performs SELECT query
    result = []
    for a in accounts:
        result.append(a.serialize()) # build list of Accounts as dictionaries
    return jsonify(result) # return JSON response


@bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def update(id: int):
    a = Account.query.get_or_404(id)
    if 'purpose' in request.json:
        a.purpose = request.json['purpose']
    if 'username' in request.json:
        a.username = request.json['username']
    db.session.commit()
    return jsonify(a)


@bp.route('', methods=['POST'])
def create():
    if 'username' not in request.json or 'password' not in request.json:
        return abort(400)
    if len(request.json['username']) < 3 or len(request.json['password']) < 8:
        return abort(400)

    a = Account(
        username=request.json['username'],
        purpose=request.json['purpose'],
        customer_id=request.json['customer_id'],
        password=scramble(request.json['password'])
)

    db.session.add(a)
    db.session.commit()

    return jsonify(a.serialize())


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    u = Account.query.get_or_404(id)
    try:
        db.session.delete(u)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)
