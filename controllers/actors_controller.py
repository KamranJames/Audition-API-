from flask import Blueprint, request
from init import db
from models.actor import Actor, ActorSchema

## ACTORS CONTROLLER


## Parameters for blueprint 
actors_bp = Blueprint('actors', __name__, url_prefix='/actors')

@actors_bp.route('/')
##@jwt_required()
def get_all_actors():
    ##if not authorize():
        ##return {'error': 'You must be an admin'}, 401 
    
    stmt = db.select(Actor)
    actors = db.session.scalars(stmt)
    return ActorSchema(many=True).dump(actors)


##Get a single actor from db
@actors_bp.route('/<int:id>/')
def one_actor(id):
    stmt = db.select(Actor).filter_by(id=id)
    actor = db.session.scalar(stmt)
    return ActorSchema().dump(actor)

##Create a single actor
@actors_bp.route('/', methods=['POST'])
##@jwt_required()
def create_one_actor():
    # Create a new actor model instance
    data = ActorSchema().load(request.json)
        
    actor = Actor(
        f_name = data['f_name'],
        l_name = data['l_name'],
        agency = data['agency'], 
       ## user_id = get_jwt_identity()
    )
    # Add & commit actor to Database
    db.session.add(actor)
    db.session.commit()
    
    return ActorSchema().dump(actor), 201

@actors_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
##@jwt_required()
def update_one_actor(id):
    ##authorize()
    stmt = db.select(Actor).filter_by(id=id)
    actor = db.session.scalar(stmt)
    if actor:
        actor.f_name = request.json.get('f_name') or actor.f_name
        actor.l_name = request.json.get('l_name') or actor.l_name
        actor.agency = request.json.get('agency') or actor.agency
        db.session.commit()      
        return ActorSchema().dump(actor)
    else:
        return {'error': f'Actor not found with id {id}'}, 404




## Delete an actor from db
@actors_bp.route('/<int:id>/', methods=['DELETE'])
##@jwt_required()
def delete_one_actor(id):
    ##authorize()

    stmt = db.select(Actor).filter_by(id=id)
    actor = db.session.scalar(stmt)
    if actor:
        db.session.delete(actor)
        db.session.commit()
        return {'message': f"Actor '{actor.f_name, actor.l_name} 'deleted successfully"}
    else:
        return {'error': f'Actor not found with id {id}'}, 404