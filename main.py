from flask import Flask
from init import db, ma, bcrypt, jwt
from marshmallow.exceptions import ValidationError
from controllers.cli_controller import db_commands
from controllers.users_controller import users_bp
from controllers.actors_controller import actors_bp
from controllers.castings_controller import castings_bp
from controllers.projects_controller import projects_bp
from controllers.auth_controller import auth_bp
from controllers.role_controller import roles_bp
import os



def create_app():
   app = Flask(__name__)
  

  ##Error handlers
 
   @app.errorhandler(ValidationError)
   def validation_error(err):
        return {'error': err.messages}, 400

   @app.errorhandler(400)
   def bad_request(err):
        return {'error': str(err)}, 400

   @app.errorhandler(404)
   def not_found(err):
        return {'error': str(err)}, 404

   @app.errorhandler(401)
   def unauthorized(err):
        return {'error': 'You are not authorized to perform this action'}, 401

   @app.errorhandler(KeyError)
   def key_error(err):
       return {'error': f'The field {err} is required.'}, 400
      
   
   ##Config Section for app

   app.config['JSON_SORT_KEYS'] = False
   app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
   app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
   

   db.init_app(app)
   ma.init_app(app)
   bcrypt.init_app(app)
   jwt.init_app(app)

   app.register_blueprint(users_bp)
   app.register_blueprint(actors_bp)
   app.register_blueprint(projects_bp)
   app.register_blueprint(castings_bp)
   app.register_blueprint(db_commands)
   app.register_blueprint(auth_bp)
   app.register_blueprint(roles_bp)

   return app 


