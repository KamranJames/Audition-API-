from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from init import db, ma
from controllers.users_controller import users_bp
from controllers.actors_controller import actors_bp
from controllers.castings_controller import castings_bp
from controllers.projects_controller import projects_bp

import os

##from flask_bcrypt import Bcrypt
##from sqlalchemy.exc import IntegrityError


def create_app():
   app = Flask(__name__)
  

  ## APP WIDE Error handler/catches all 404 errors/converts to json
   @app.errorhandler(404)
   def not_found(err):
      return {'error': str(err)}, 404
      
   
   ## Turns off alphabetical sorting
   app.config ['JSON_SORT_KEYS'] = False

   ## Sets our apps URI - to whats in our .env 
   app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
   db.init_app(app)
   ma.init_app(app)

   app.register_blueprint(users_bp)
   app.register_blueprint(actors_bp)
   app.register_blueprint(projects_bp)
   app.register_blueprint(castings_bp)

   return app 