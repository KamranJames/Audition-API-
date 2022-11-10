from flask import Blueprint
from init import db ,bcrypt
from models.user import User
from models.actor import Actor
from models.project import Project
from models.role import Role
from models.casting import Casting
from models.comment import Comment
from datetime import datetime



db_commands = Blueprint('db', __name__)


@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables created")

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command('seed')
def seed_db():
    users = [
        User(
            name ='John Waters',
            email='johnwaters@gmail.com',
            password=bcrypt.generate_password_hash('coder').decode('utf-8'),
            is_admin=True
        ),

        User(
            name=['Jack Reacher'],
            email=['jack@reacher.com'],
            password=bcrypt.generate_password_hash('kitten').decode('utf-8'),
        )
    ]

    db.session.add_all(users)
    db.session.commit()

    print('Tables seeded')

## Create example projects
    projects = [
        Project(
            name = 'The last days',
            director = 'John Mckin',
            year = '2022',
            status = 'Filming',
            user_id = users[0].id
        
        ),
        Project(
            name = 'Sephiroth Returns',
            director = 'Cal Kestis',
            year = '2023',
            status = 'Pre-production',
            user_id = users[1].id
        
        )
    ]

    db.session.add_all(projects)
    db.session.commit()

    print('Tables seeded')

## Create example actors
    actors = [
        Actor(
            f_name = 'Jerry',
            l_name = 'Arrow',
            agency = 'NBD Agency',
            project_id = projects[0].id,
         
        ),
        Actor(
            f_name = 'Jonah',
            l_name = 'Loanal',
            agency = 'Sigma Agency',
            project_id = projects[1].id,
          
        ),
        Actor(
            f_name = 'Jon',
            l_name = 'Loss',
            agency = 'NBD Agency',
            project_id = projects[1].id,
           
        )
    ]

    db.session.add_all(actors)
    db.session.commit()


## Create example roles
    roles = [
        Role(
            name = 'Zombie man',
            notes = 'Searching for any gender, any ages, dance ability is a plus.',
            project_id = projects[0].id,
            actor_id = actors[0].id
        ),
        Role(
            name = 'Sephiroths son',
            notes = 'Searching for a male, ages 25 to 30, martial arts experience required.',
            project_id = projects[1].id,
            actor_id = actors[1].id
        )
    ]

    db.session.add_all(roles)
    db.session.commit()

    print('Tables seeded')

   ## Create example Castings
    castings = [
        Casting(
            casting_assosciate= 'Victory Casting',
            location = 'Vancouver, Canada',
            agency = 'NBD Agency',
            project_id = projects[1].id,
        ),
        Casting(
            casting_assosciate= 'Mallory White',
            location = 'Los Angeles, America',
            agency = 'CPJ Agency',
            project_id = projects[0].id
        )
    ]

    db.session.add_all(castings)
    db.session.commit()

    ## Create example Comment
    comments = [
        Comment(
           message = 'This project has a budget of 100 million and is shooting in Los Angeles in December.',
           date = datetime.today(),
           project_id = projects[0].id,
           user_id = users[0].id
        ),
        Comment(
            message = 'This project is a low budget independent feature. It will be shot and around Vancouver, Canada in order to get tax breaks.',
            date = datetime.today(),
            project_id = projects[1].id,
            user_id = users[1].id
        )
    ]

    db.session.add_all(comments)
    db.session.commit()




