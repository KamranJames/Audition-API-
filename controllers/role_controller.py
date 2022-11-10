from flask import Blueprint, request
from init import db
from models.role import Role, RoleSchema

## ROLE CONTROLLER


## Parameters for our blueprint 
roles_bp = Blueprint('roles', __name__, url_prefix='/roles')

#Get all roles
@roles_bp.route('/')
##@jwt_required()
def get_all_roles():
    ##if not authorize():
        ##return {'error': 'You must be an admin'}, 401 
    
    stmt = db.select(Role)
    roles = db.session.scalars(stmt)
    return RoleSchema(many=True).dump(roles)


## Select one role 
@roles_bp.route('/<int:id>/')
def get_one_role(id):
    stmt = db.select(Role).filter_by(id=id)
    role = db.session.scalar(stmt)
    if role:
        return RoleSchema().dump(role)
    else:
        return {'error': f'Role not found with id {id}'}, 404


#Edit a single role
@roles_bp.route('/<int:id>/', methods = ['PUT', 'PATCH'])
#@jwt_required()
def update_one_role(id):
    ##authorize()
    stmt = db.select(Role).filter_by(id=id)
    role = db.session.scalar(stmt)
    if role:
       role.name = request.json.get('name') or role.name
       role.notes = request.json.get('notes') or role.notes
       db.session.commit()
       return RoleSchema().dump(role)
    else: 
        return {'error': f'Role not found with {id}'}, 404


#Create a single role
@roles_bp.route('/', methods=['POST'])
##@jwt_required()
def create_one_role():
    # Create a new role instance
    data = RoleSchema().load(request.json)
        
    role = Role(
        name = data['name'],
        notes = data['notes'],
        ## user_id = get_jwt_identity()
    )
    # Add & commit project to Database
    db.session.add(role)
    db.session.commit()
    
    return RoleSchema().dump(role), 201



## Delete a role from db
@roles_bp.route('/<int:id>/', methods=['DELETE'])
##@jwt_required()
def delete_one_role(id):
    ##authorize()

    stmt = db.select(Role).filter_by(id=id)
    role = db.session.scalar(stmt)
    if role:
        db.session.delete(role)
        db.session.commit()
        return {'message': f'Role {role.name} deleted successfully'}
    else:
        return {'error': f'Role not found with id {id}'}, 404





    