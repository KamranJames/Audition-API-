from flask import Blueprint
from init import db
from models.project import Project, ProjectSchema

## Project CONTROLLER


## Parameters for our blueprint 
projects_bp = Blueprint('projects', __name__, url_prefix='/projects')

projects_bp.route('/')
##@jwt_required()
def all_projects():
    ##if not authorize():
        ##return {'error': 'You must be an admin'}, 401 
    
    stmt = db.select(Project).order_by(Project.desc(), Project.title)
    projects = db.session.scalars(stmt)
    return ProjectSchema(many=True).dump(projects)

## Will auto convert whatever request comes in as an int

## Allows us to select a project by the id from db
@projects_bp.route('/<int:id>/')
def one_project(id):
    stmt = db.select(Project).filer_by(id=id)
    project = db.session.scalar(stmt)
    return ProjectSchema().dump(project)