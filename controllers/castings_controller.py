from flask import Blueprint, request
from init import db
from models.casting import Casting, CastingSchema

## Casting Controller


## Parameters for our blueprint 
castings_bp = Blueprint('castings', __name__, url_prefix='/castings')

@castings_bp.route('/')
##@jwt_required()
def all_castings():
    ##if not authorize():
        ##return {'error': 'You must be an admin'}, 401 
    
    stmt = db.select(Casting)
    castings = db.session.scalars(stmt)
    return CastingSchema(many=True).dump(castings)



##Get a single casting
@castings_bp.route('/<int:id>/')
def one_casting(id):
    stmt = db.select(Casting).filter_by(id=id)
    casting = db.session.scalar(stmt)
    return CastingSchema().dump(casting)


##Create a single casting
@castings_bp.route('/', methods=['POST'])
##@jwt_required()
def create_one_casting():
    # Create a new casting model instance
    data = CastingSchema().load(request.json)
        
    casting = Casting(
        ##authorize()
        cd = data['cd'],
        location = data['location'],
       ## user_id = get_jwt_identity()
    )
    # Add & commit casting to Database
    db.session.add(casting)
    db.session.commit()
    
    return CastingSchema().dump(casting), 201

## Edit a casting
@castings_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
##@jwt_required()
def update_one_casting(id):
    ##authorize()
    stmt = db.select(Casting).filter_by(id=id)
    casting = db.session.scalar(stmt)
    if casting:
        casting.cd = request.json.get('cd') or casting.cd
        casting.location = request.json.get('location') or casting.location
        db.session.commit()      
        return CastingSchema().dump(casting)
    else:
        return {'error': f'Casting not found with id {id}'}, 404




## Delete a casting from db
@castings_bp.route('/<int:id>/', methods=['DELETE'])
##@jwt_required()
def delete_one_casting(id):
    ##authorize()

    stmt = db.select(Casting).filter_by(id=id)
    casting = db.session.scalar(stmt)
    if casting:
        db.session.delete(casting)
        db.session.commit()
        return {'message': f"Casting '{casting.cd, casting.location} 'deleted successfully"}
    else:
        return {'error': f'Casting not found with id {id}'}, 404