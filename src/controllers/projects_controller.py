from flask import Blueprint, request
from init import db
from models.project import Project, ProjectSchema
from models.comment import Comment, CommentSchema
from models.user import User, UserSchema
from datetime import date
from controllers.auth_controller import authorize
from flask_jwt_extended import jwt_required, get_jwt_identity


## Project CONTROLLER

## Parameters for our blueprint 
projects_bp = Blueprint('projects', __name__, url_prefix='/projects')

#Get all projects from db
@projects_bp.route('/')
@jwt_required()
def get_all_projects():
    
    stmt = db.select(Project)
    projects = db.session.scalars(stmt)
    return ProjectSchema(many=True, exclude=['user_id']).dump(projects)


## Select a project by the id from db
@projects_bp.route('/<int:id>/')
@jwt_required()
def get_one_project(id):
    stmt = db.select(Project).filter_by(id=id)
    project = db.session.scalar(stmt)
    if project:
        return ProjectSchema(exclude=['user_id']).dump(project)
    else:
        return {'error': f'Project not found with id {id}'}, 404
 


#Edit a single project
@projects_bp.route('/<int:id>/', methods = ['PUT', 'PATCH'])
@jwt_required()
##Check to see if user has admin permissions.
def update_one_project(id):
    stmt = db.select(Project).filter_by(id=id)
    project = db.session.scalar(stmt)
    if project:
       project.name = request.json.get('name') or project.name
       project.director = request.json.get('director') or project.director
       project.year = request.json.get('year') or project.year
       project.status = request.json.get('status') or project.status
       ##Requires authorizatiion
       authorize(User.is_admin)
       db.session.commit()
       return ProjectSchema().dump(project)
    else: 
        return {'error': f'Project not found with {id}'}, 404


#Create a single project
@projects_bp.route('/', methods=['POST'])
@jwt_required()
def create_one_project():
    data = ProjectSchema().load(request.json)
        
    project = Project(
        name = data['name'],
        director = data['director'],
        year = data['year'], 
        status = data['status']
    )
    # Add & commit project to Database
    db.session.add(project)
    db.session.commit()
    
    return ProjectSchema().dump(project), 201


## Delete a project from db
@projects_bp.route('/<int:id>/', methods=['DELETE'])
@jwt_required()
def delete_one_project(id):
    

    stmt = db.select(Project).filter_by(id=id)
    project = db.session.scalar(stmt)
    if project:
        authorize(User.is_admin)
        db.session.delete(project)
        db.session.commit()
        return {'message': f'Project {project.name} deleted successfully'}
    else:
        return {'error': f'Project not found with id {id}'}, 404

## Add comments to a project
@projects_bp.route('/<int:project_id>/comments', methods=['POST'])
@jwt_required()
def create_comment(project_id):
    stmt = db.select(Project).filter_by(id=project_id)
    project = db.session.scalar(stmt)
    if project:
        comment = Comment(
            message = request.json['message'],
            user_id = get_jwt_identity(),
            project = project,
            date = date.today()
        )
        db.session.add(comment)
        db.session.commit()
        return CommentSchema().dump(comment), 201
    else:
        return {'error': f'Project not found with id {id}'}, 404

## Gets all comments for a project
@projects_bp.route('/comments', methods=['GET'])
@jwt_required()
def get_all_comments():
    
    stmt = db.select(Comment)
    comments = db.session.scalars(stmt)
    return CommentSchema(many=True).dump(comments)







