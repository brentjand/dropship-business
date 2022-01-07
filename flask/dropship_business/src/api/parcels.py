from flask import Blueprint, jsonify, abort, request


from ..models import Parcel, db



bp = Blueprint('parcels', __name__, url_prefix='/parcels')


@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    parcels = Parcel.query.all() # ORM performs SELECT query
    result = []
    for p in parcels:
        result.append(p.serialize()) # build list of Accounts as dictionaries
    return jsonify(result) # return JSON response