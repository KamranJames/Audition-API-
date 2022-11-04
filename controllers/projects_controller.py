from flask import Blueprint, request
from init import db
from models.project import Project, ProjectSchema

## Project CONTROLLER


## Parameters for our blueprint 
projects_bp = Blueprint('projects', __name__, url_prefix='/projects')

projects_bp.route('/')
##@jwt_required()
def get_all_projects():
    ##if not authorize():
        ##return {'error': 'You must be an admin'}, 401 
    
    stmt = db.select(Project).order_by(Project.desc(), Project.title)
    projects = db.session.scalars(stmt)
    return ProjectSchema(many=True).dump(projects)

## Will auto convert whatever request comes in as an int

## Select a project by the id from db
@projects_bp.route('/<int:id>/')
def get_one_project(id):
    stmt = db.select(Project).filter_by(id=id)
    project = db.session.scalar(stmt)
    return ProjectSchema().dump(project)




#Edit a single project
@projects_bp.route('/<int:id>/', methods = ['PUT', 'PATCH'])
def update_one_project(id):
    stmt = db.select(Project).filter_by(id=id)
    project = db.session.scalar(stmt)
    if project:
       project.name = request.json.get['name'] or project.name
       project.director = request.json.get['director'] or project.director
       project.year = request.json.get['year'] or project.year
       db.session.commit()
       return ProjectSchema().dump(project)
    else: 
        return {'error': f'Project not found with {id}'}, 404






    