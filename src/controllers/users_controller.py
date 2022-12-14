from flask import Blueprint, request
from init import db, bcrypt
from datetime import date
from models.user import User, UserSchema
from sqlalchemy.exc import IntegrityError
from controllers.auth_controller import authorize
from flask_jwt_extended import jwt_required, get_jwt_identity

## USERS CONTROLLER

## Parameters for our blueprint 
users_bp = Blueprint('users', __name__, url_prefix='/users')

#Get all users
@users_bp.route('/')
@jwt_required()
def get_all_users():
    stmt = db.select(User)
    user = db.session.scalars(stmt)
    authorize(User.is_admin)
    return UserSchema(many=True).dump(user)


## Get one user from db 

@users_bp.route('/<int:id>/')
@jwt_required()
def get_one_user(id):
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    if user:
        authorize(User.is_admin)
        return UserSchema().dump(user)
    else:
        return {'error': f'User not found with id {id}'}, 404



#Edit one user in db
@users_bp.route('/<int:id>/', methods = ['PUT, PATCH'])
@jwt_required()
def edit_user(id):
    
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    if user: 
        user.name = request.json.get('name') or user.name
        user.email = request.json.get('email') or user.email
        user.password = request.json.get('password') or user.password
        user.is_admin = request.json.get('is_admin') or user.is_admin
        authorize(User.is_admin)
        db.session.commit()      
        return {'message': "User info changed successfully"}
    else:
        return {'error': f'User not found with id {id}'}, 404

## Delete a user from db
@users_bp.route('/<int:id>/', methods=['DELETE'])
@jwt_required()
def delete_one_user(id):
    

    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    if user:
        ##authorize(User.is_admin)
        db.session.delete(user)
        db.session.commit()
        return {'message': f'User {user.name} deleted successfully'}
    else:
        return {'error': f'User not found with id {id}'}, 404


#Edit a single user
@users_bp.route('/<int:id>/', methods = ['PUT', 'PATCH'])
@jwt_required()
##Check to see if user has admin permissions.
def update_one_user(id):
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    if user:
       user.name = request.json.get('name') or user.name
       user.email = request.json.get('email') or user.email
       user.password = request.json.get('password') or user.password
       ##Requires authorizatiion
       authorize(User.is_admin)
       db.session.commit()
       return UserSchema().dump(user)
    else: 
        return {'error': f'User not found with {id}'}, 404

        

