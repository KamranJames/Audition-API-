from flask import Blueprint, request
from init import db
from models.casting import Casting, CastingSchema
from controllers.auth_controller import authorize
from models.user import User, UserSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

## Casting Controller


## Parameters for our blueprint 
castings_bp = Blueprint('castings', __name__, url_prefix='/castings')

## Get all castings
@castings_bp.route('/')
@jwt_required()
def get_all_castings():
    
    stmt = db.select(Casting)
    castings = db.session.scalars(stmt)
    return CastingSchema(many=True).dump(castings)


##Select One casting
@castings_bp.route('/<int:id>/')
def get_one_casting(id):
    stmt = db.select(Casting).filter_by(id=id)
    casting = db.session.scalar(stmt)
    return CastingSchema().dump(casting)


##Create a single casting
@castings_bp.route('/', methods=['POST'])
@jwt_required()
def create_one_casting():
    # Create a new casting model instance
    data = CastingSchema().load(request.json)
        
    casting = Casting(
        casting_assosciate = data['casting_assosciate'],
        location = data['location'],
        agency = data['agency'],
        project_id = data['project_id']

    )
    # Add & commit casting to Database
    db.session.add(casting)
    db.session.commit()
    
    return CastingSchema().dump(casting), 201

## Edit a casting
@castings_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_casting(id):
    stmt = db.select(Casting).filter_by(id=id)
    casting = db.session.scalar(stmt)
    if casting:
        casting.casting_assosciate = request.json.get('casting_assosciate') or casting.casting_assosciate
        casting.location = request.json.get('location') or casting.location
        casting.agency = request.json.get('agency') or casting.agency
        authorize(User.is_admin)
        db.session.commit()      
        return CastingSchema().dump(casting)
    else:
        return {'error': f'Casting not found with id {id}'}, 404




## Delete a casting from db
@castings_bp.route('/<int:id>/', methods=['DELETE'])
@jwt_required()
def delete_one_casting(id):

    stmt = db.select(Casting).filter_by(id=id)
    casting = db.session.scalar(stmt)
    if casting:
        authorize(User.is_admin)
        db.session.delete(casting)
        db.session.commit()
        return {'message': f"Casting '{casting.casting_assosciate} 'deleted successfully"}
    else:
        return {'error': f'Casting not found with id {id}'}, 404