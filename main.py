from flask import Flask, jsonify, request 
from flask_sqlalchemy import SQLAlchemy
from db import db, ma
from controllers.users_controller import users_bp
import os

##from flask_bcrypt import Bcrypt
##from sqlalchemy.exc import IntegrityError


def create_app():
   app = Flask(__name__)
   
   ## Turns off alphabetical sorting
   app.config ['JSON_SORT_KEYS'] = False
   ## Sets our apps URI - to whats in our .env 
   app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
   
   db.init_app(app)
   ma.init_app(app)

   app.register_blueprint(users_bp)

   return app 