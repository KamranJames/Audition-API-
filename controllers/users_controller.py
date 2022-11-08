from flask import Blueprint, request
from init import db, bcrypt
from models.user import User, UserSchema
from sqlalchemy.exc import IntegrityError
from controllers.auth_controller import authorize
from flask_jwt_extended import jwt_required, get_jwt_identity

## USERS CONTROLLER

## Parameters for our blueprint 
users_bp = Blueprint('users', __name__, url_prefix='/users')

#Get all users/requires authentication & authorization
@users_bp.route('/')
@jwt_required()
def get_all_users():
    if not authorize():
        return {'error': 'You must be an admin'}, 401 
    
    stmt = db.select(User).order_by(User.desc(), User.title)
    users = db.session.scalars(stmt)
    if User: 
           return UserSchema.dump()
    return UserSchema(many=True).dump(users)


## Get a single user
@users_bp.route('/<int:id>/')
def get_one_user(id):
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    if user:
        return UserSchema().dump(user)
    else:
        return {'error': f'User not found with id {id}'}, 404

## Create a new user
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

#Delete a user from the db
@users_bp.route('/<int:id>/', methods = ['DELETE'])
@jwt_required()
def delete_one_user(id):
    if not authorize():
        return {'error': 'You must be an admin'}, 401 
    
    stmt = db.select(User).filter_by(id=id)
    users = db.session.scalar(stmt)
    if User: 
        #Delete and commit changes to db
           db.session.delete(User)
           db.session.commit()
           return {'message': f"User '{User.title}' deleted successfully"}
    else:
        return {'error': f'User not found with id {id}'}, 404

#Edit one user in db
@users_bp.route('/<int:id>/', methods = ['PUT, PATCH'])
@jwt_required()
def edit_user(id):
    if not authorize():
        return {'error': 'You must be an admin'}, 401 
    
    stmt = db.select(User).filter_by(id=id)
    users = db.session.scalar(stmt)
    if User: 
        #Edit and commit changes to db
           db.session.commit()
           return {'message': f"User '{User.title}' changed successfully"}
    else:
        return {'error': f'User not found with id {id}'}, 404

