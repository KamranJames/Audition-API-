from flask import Blueprint, request
from init import db
from models.role import Role, RoleSchema
from models.project import Project, ProjectSchema

## ROLE CONTROLLER


## Parameters for our blueprint 
roles_bp = Blueprint('roles', __name__, url_prefix='/roles')

@roles_bp.route('/')
##@jwt_required()
def get_all_roles():
    ##if not authorize():
        ##return {'error': 'You must be an admin'}, 401 
    
    stmt = db.select(Role).order_by(Role.desc(), Role.title)
    roles = db.session.scalars(stmt)
    return RoleSchema(many=True).dump(roles)


## Select a role by the id from db
@roles_bp.route('/<int:id>/')
def get_one_role(id):
    stmt = db.select(Role).filter_by(id=id)
    role = db.session.scalar(stmt)
    return RoleSchema().dump(role)


#Edit a single role
@roles_bp.route('/<int:id>/', methods = ['PUT', 'PATCH'])
#@jwt_required()
def update_one_role(id):
    stmt = db.select(Role).filter_by(id=id)
    role = db.session.scalar(stmt)
    if role:
       role.role = request.json.get('role') or role.role
       project.name = request.json.get('name') or project.name
       db.session.commit()
       return ProjectSchema().dump(project)
    else: 
        return {'error': f'Project not found with {id}'}, 404


#Create a single project
@roles_bp.route('/', methods=['POST'])
##@jwt_required()
def create_one_role():
    # Create a new role model instance
    data = RoleSchema().load(request.json)
        
    role = Role(
        role = data['role']
       ## user_id = get_jwt_identity()
    )
    # Add & commit project to Database
    db.session.add(role)
    db.session.commit()
    
    return ProjectSchema().dump(role), 201



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
        return {'message': f"Role {role.role} deleted successfully"}
    else:
        return {'error': f'Role not found with id {id}'}, 404





    