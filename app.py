from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
##db= SQLAlchemy(app)

##app.config ['JSON_SORT_KEYS'] = False
##app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
##app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')

@app.route('/')
def index():
    return "Hello world"

class Audition(db.model):
     __tablename__ = "auditions"

     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String, nullable=False)
     date = db.Column(db.Date, nullable=False)
     #learn how to join the FK below with the assosciated models.
     ##Fk casting_director_id
     ##Fk actor_id
