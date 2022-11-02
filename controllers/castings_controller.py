from flask import Blueprint
from init import db
from models.casting import Casting, CastingSchema

## Project CONTROLLER


## Parameters for our blueprint 
castings_bp = Blueprint('castings', __name__, url_prefix='/castings')

castings_bp.route('/')
##@jwt_required()
def all_castings():
    ##if not authorize():
        ##return {'error': 'You must be an admin'}, 401 
    
    stmt = db.select(Casting).order_by(Casting.desc(), Casting.title)
    castings = db.session.scalars(stmt)
    return CastingSchema(many=True).dump(castings)

## Will auto convert whatever request comes in as an int

## Allows us to select a casting by the id from db
@castings_bp.route('/<int:id>/')
def one_casting(id):
    stmt = db.select(Casting).filer_by(id=id)
    casting = db.session.scalar(stmt)
    return CastingSchema().dump(casting)