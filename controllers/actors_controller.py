from flask import Blueprint
from init import db
from models.actor import Actor, ActorSchema

## ACTORS CONTROLLER


## Parameters for our blueprint 
actors_bp = Blueprint('actors', __name__, url_prefix='/actors')

actors_bp.route('/')
##@jwt_required()
def all_actors():
    ##if not authorize():
        ##return {'error': 'You must be an admin'}, 401 
    
    stmt = db.select(Actor).order_by(Actor.desc(), Actor.title)
    actors = db.session.scalars(stmt)
    return ActorSchema(many=True).dump(actors)

## Will auto convert whatever request comes in as an int

## Allows us to select a user by their id from db
@actors_bp.route('/<int:id>/')
def one_actor(id):
    stmt = db.select(Actor).filer_by(id=id)
    actor = db.session.scalar(stmt)
    return ActorSchema().dump(actor)