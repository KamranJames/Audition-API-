from init import db, ma

## User Model 
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

# User Schema 
class UserSchema(ma.Schema):
    class Meta:
        #model = User
        fields = ('id', 'name', 'email', 'password', 'is_admin')
        #ordered = True

#User_schema = UserSchema()
#User_schema = UserSchema(many=True)

