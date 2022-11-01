from flask import Flask, jsonify, request 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow



app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://db_dev:passwordcoder@127.0.01:5432/auditiondb'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config ['JSON_SORT_KEYS'] = False
##app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
##app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')

db = SQLAlchemy(app)
ma = Marshmallow()


@app.route('/')
def index():
    return "Hello world"

@app.route('/auditions/')
def all_auditions():
    stmt = db.select(Audition).order_by(Audition.desc(), Audition.title)
    auditions = db.session.scalars(stmt)
    ## Scalars returns all, if we want one use scalar.
    return AuditionSchema(many=True).dump(auditions)


## TEST FOR AUTH 
class Users(db.Model):
      __tablename__ = 'users'

      id = db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String)
      email = db.Column(db.String, unique = True)
      ## NOT NULL/ NEED A PASSWORD
      password = db.Column(db.String, nullable=False)
      ## Default the admin is FALSE.
      is_admin = db.Column(db.Boolean, default=False) 
    
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'is_admin')



class Audition(db.Model):
     __tablename__ = "auditions"

     id = db.Column(db.Integer, primary_key=True)
     project = db.Column(db.String, nullable=False)
     role = db.Column(db.String, nullable=False)
     date = db.Column(db.Date, nullable=False)
     comments = db.Column(db.String)

     #learn how to join the FK below with the assosciated models.
     ##Fk casting_director_id
     ##Fk actor_id

class Casting(db.Model):
     __tablename__ = "castings"

     id = db.Column(db.Integer, primary_key=True)
     director = db.Column(db.String, nullable=False)
     location = db.Column(db.String, nullable=False)


class Actor(db.Model):
     __tablename__ = "actors"

     id = db.Column(db.Integer, primary_key=True)
     f_name = db.Column(db.String, nullable=False)
     l_name = db.Column(db.String, nullable=False)
     agency = db.Column(db.String, nullable=False)
     ## Learn how to add FK here audition_id


## SCHEMAS 

## Audition Schema 
class AuditionSchema(ma.Schema):
    class Meta:
        model = Audition

    fields = ("project", "role", "date", "comments")    

audition_schema = AuditionSchema()
audition_schema = AuditionSchema(many=True)

## Casting Schema
class CastingSchema(ma.Schema):
    class Meta:
        model = Casting
        
    fields = ("director", "location",)    

casting_schema = CastingSchema()
casting_schema = CastingSchema(many=True)

## Acting Schema
class ActorSchema(ma.Schema):
    class Meta:
        model = Actor

    fields = ("f_name", "l_name", 'agency')    

audition_schema = ActorSchema()
audition_schema = ActorSchema(many=True)

## Creates our tables
@app.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")
 # Drops a table from the database
@app.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")

## TO DO Add date functions

 # Seeds our Database
 ## EXAMPLE AUDITIONS
@app.cli.command('seed')
def seed_db():
    auditions = [
        Audition(
            project = 'Untitled Batman project',
            role = 'Mr Freeze',
            date = '07/04/2025',
            comments = 'The Casting director asked me to do a second take. In this take they requested I scream when I see Batman.',
            ),
        Audition(
            project = 'The Last of us',
            role = 'Zombie',
            date = '07/04/2023',
            comments = 'In the audition I decided to improvise a line as the zombie, I went "Argh". Director responded well.',
        )
    ]
            
    
    db.session.add_all(auditions)
    db.session.commit()
    print('Tables Seeded')