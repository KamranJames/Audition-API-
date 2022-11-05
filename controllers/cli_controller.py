from flask import Blueprint
from init import db ,bcrypt
from models.user import User
from models.actor import Actor
from models.project import Project
from models.role import Role


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
            email='johnwaters@gmail.com',
            password=bcrypt.generate_password_hash('coder').decode('utf-8'),
            is_admin=True
        ),
        User(
            name='Jack Reacher',
            email='jack@reacher.com',
            password=bcrypt.generate_password_hash('coder').decode('utf-8')
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
        ),
        Project(
            name = 'Sephiroth Returns',
            director = 'Cal Kestis ',
            year = '2022',
        )
    ]

    db.session.add_all(projects)
    db.session.commit()

    print('Tables seeded')

## Create example roles
    roles = [
        Role(
            role = 'Zombie man',
            ##project = projects[0]
        ),
        Role(
            role = 'Sephiroth/s son',
            ##project = projects[1]
        )
    ]

    db.session.add_all(roles)
    db.session.commit()

    print('Tables seeded')

## Create example actors
    actors = [
        Actor(
            f_name = 'Jerry',
            l_name = 'Arrow',
            agency = 'NBD Agency'
            ##project = projects[0],
            ##role = roles[0],
        ),
        Actor(
            f_name = 'Jerry Arrow',
            l_name = 'Arrow',
            agency = 'NBD Agency',
            ##project = projects[1],
            ##role = roles[1],
        )
    ]

    db.session.add_all(actors)
    db.session.commit()

    print('Tables seeded')