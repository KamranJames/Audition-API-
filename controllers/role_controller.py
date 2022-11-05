from flask import Blueprint, request
from init import db
from models.role import Role, RoleSchema

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