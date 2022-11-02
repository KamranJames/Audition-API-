from flask import Blueprint, request
from flask_bcrypt import Bcrypt
from init import db
from models.user import User, UserSchema
from sqlalchemy.exc import IntegrityError

## USERS CONTROLLER

bcrypt = Bcrypt()
## Parameters for our blueprint 
users_bp = Blueprint('users', __name__, url_prefix='/users')

users_bp.route('/')
##@jwt_required()
def all_users():
    ##if not authorize():
        ##return {'error': 'You must be an admin'}, 401 
    
    stmt = db.select(User).order_by(User.desc(), User.title)
    users = db.session.scalars(stmt)
    if user: 
           return UserSchema.dump()
    return UserSchema(many=True).dump(users)

## Will auto convert whatever request comes in as an int

## Allows us to select a user by their id from db
@users_bp.route('/<int:id>/')
def one_user(id):
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    if user:
        return UserSchema().dump(user)
    else:
        return {'error': f'User not found with id {id}'}, 404

@users_bp.route('/', methods=['POST'])
def auth_register():
    try:
        # Create a new User model instance
        user = User(
            name = request.json['name'],
            email=request.json['email'],
            password=bcrypt.generate_password_hash(request.json['password']).decode('utf-8')
        )
        # Add & commit user to Database
        db.session.add(user)
        db.session.commit()
        return UserSchema(exclude=['password']).dump(user), 201
        #Error message if user is already registered.
    except IntegrityError:
        return {'error': 'Email address already in use'}, 409