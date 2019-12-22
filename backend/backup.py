from datetime import datetime
from flask import jsonify, request
from flask_api import FlaskAPI, status
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_pymongo import PyMongo
import os



app = FlaskAPI(__name__)

app.config['MONGO_DBNAME'] = os.getenv("MONGO_DBNAME")
app.config['MONGO_URI'] = os.getenv("MONGO_URI")
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")

bcrypt = Bcrypt(app)
jwt = JWTManager(app)
mongo = PyMongo(app)

# TODO: Check for SQL Injects, email is actual email, check if username/email exists
@app.route('/api/users/signup', methods=['POST'])
def signup():
    users = mongo.db.users
    user_name = request.get_json()['user_name']
    first_name = request.get_json()['first_name']
    last_name = request.get_json()['last_name']
    email = request.get_json()['email']
    password = bcrypt.generate_password_hash(request.get_json()['password']).decode('utf-8')
    date_created = datetime.utcnow()

    userObj = users.insert({
        'user_name': user_name,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password,
        'date_created': date_created
    })

    checkUser = users.find_one({'_id': userObj})

    result = jsonify({'email': checkUser['email'] + ' registered'})

    return result, status.HTTP_201_CREATED

# TODO check for SQL Inject
@app.route('/api/users/login', methods=['POST'])
def login():
    users = mongo.db.users
    user_name = request.get_json()['user_name']
    password = request.get_json()['password']
    result = ""

    checkUser = users.find_one({'user_name': user_name})

    if checkUser:
        if bcrypt.check_password_hash(checkUser['password'], password):
            token = create_access_token(identity={
                'user_name': checkUser['user_name'],
            })
            result = jsonify({"token": token})
            return result, status.HTTP_202_ACCEPTED
        else:
            result = jsonify({"error": "Password invalid"})
            return result, status.HTTP_401_UNAUTHORIZED
    else:
        result = jsonify({"error": "Username not found"})
        return result, status.HTTP_401_UNAUTHORIZED

# TODO: Return data stored in another collection    
@app.route('/api/dashboard', methods=['GET'])
@jwt_required
def dashboard():
    current_user = get_jwt_identity()
    result = jsonify(loggin_in_as=current_user)
    return result, status.HTTP_200_OK

if __name__ == '__main__':
    app.run(debug=True)
