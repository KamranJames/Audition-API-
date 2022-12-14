from flask import Blueprint, request, abort
from init import db, bcrypt
from datetime import timedelta
from models.user import User, UserSchema
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, get_jwt_identity

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

 ## Authorization Controller



@auth_bp.route('/register/', methods=['POST'])
def auth_register():

    #Loads requests through schema to validate
    data = UserSchema().load(request.json)

    try:
        # Create a new User model instance from the user info
        user = User(
            email = request.json['email'],
            password = bcrypt.generate_password_hash(request.json['password']).decode('utf8'),
            name = request.json['name']
        )
        # Commits an added user to db
        db.session.add(user)
        db.session.commit()
        return UserSchema(exclude=['password', 'projects', 'comments', 'is_admin'] ).dump(user), 201
    except IntegrityError:
        return {'error': 'Email address already in use'}, 409
    except KeyError:
        return {'error': 'Email or password required'}, 404


@auth_bp.route('/login/', methods=['POST'])
def auth_login():

    # Find a user by email address
    stmt = db.select(User).filter_by(email=request.json['email'])
    user = db.session.scalar(stmt)
    # If user exists and password is correct
    if user and bcrypt.check_password_hash(user.password, request.json['password']):
        # return UserSchema(exclude=['password']).dump(user)
        token = create_access_token(identity=str(user.id), expires_delta=timedelta(hours=8))
        return {'email': user.email, 'token': token, 'is_admin': user.is_admin}
    else:
        return {'error': 'Invalid email or password'}, 401

## Authorization function
def authorize(id):
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if not user.is_admin:
       abort(401)


