from flask import Blueprint, request
from init import db
from models.project import Project, ProjectSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

## Project CONTROLLER


## Parameters for our blueprint 
projects_bp = Blueprint('projects', __name__, url_prefix='/projects')


@projects_bp.route('/')
##@jwt_required()
def get_all_projects():
    ##if not authorize():
        ##return {'error': 'You must be an admin'}, 401 
    
    stmt = db.select(Project)
    projects = db.session.scalars(stmt)
    return ProjectSchema(many=True).dump(projects)


## Select a project by the id from db
@projects_bp.route('/<int:id>/')
def get_one_project(id):
    stmt = db.select(Project).filter_by(id=id)
    project = db.session.scalar(stmt)
    return ProjectSchema().dump(project)


#Edit a single project
@projects_bp.route('/<int:id>/', methods = ['PUT', 'PATCH'])
@jwt_required()
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


#Create a single project
@projects_bp.route('/', methods=['POST'])
##@jwt_required()
def create_one_project():
    # Create a new project model instance
    data = ProjectSchema().load(request.json)
        
    project = Project(
        name = data['name'],
        director = data['director'],
        year = data['year'], 
       ## user_id = get_jwt_identity()
    )
    # Add & commit project to Database
    db.session.add(project)
    db.session.commit()






    