import datetime
from myApp import app, db, bcrypt, jwt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity




class User():

    userObj = {}
    user_name = str
    first_name = str
    last_name = str
    email = str
    password = str

    def __init__(self, userObj):
        "Initialize the user object"
        self.user_name = userObj['user_name']
        self.first_name = userObj['first_name']
        self.last_name = userObj['last_name']
        self.email = userObj['email']
        self.password = bcrypt.generate_password_hash(userObj['password']).decode('utf-8')
        self.userObj = {
            "user_name": self.user_name,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password,
            "date_created": datetime.datetime.utcnow()
        }
    
    def save(self):
        user_id = db.users.insert(self.userObj)
        return user_id
    
    def createAccessToken(self):
        # Generates Bearer token
        token = create_access_token(identity={'user_name': self.user_name})
        return token
    

        
