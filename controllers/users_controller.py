from flask import Blueprint
from init import db
from models.user import User, UserSchema

## USERS CONTROLLER


## Parameters for our blueprint 
users_bp = Blueprint('users', __name__, url_prefix='/users')

users_bp.route('/')
##@jwt_required()
def all_users():
    ##if not authorize():
        ##return {'error': 'You must be an admin'}, 401 
    
    stmt = db.select(User).order_by(User.desc(), User.title)
    users = db.session.scalars(stmt)
    return UserSchema(many=True).dump(users)

## Will auto convert whatever request comes in as an int

## Allows us to select a user by their id from db
@users_bp.route('/<int:id>/')
def one_user(id):
    stmt = db.select(User).filer_by(id=id)
    user = db.session.scalar(stmt)
    return UserSchema().dump(user)