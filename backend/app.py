from datetime import datetime
from flask import jsonify, request, jsonify
from flask_api import FlaskAPI, status
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token
from flask_pymongo import PyMongo
import os

# Import dotenv
from dotenv import load_dotenv
load_dotenv()


app = FlaskAPI(__name__)

app.config['MONGO_DBNAME'] = os.getenv("MONGO_DBNAME")
app.config['MONGO_URI'] = os.getenv("MONGO_URI")
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")

bcrypt = Bcrypt(app)
#jwt = JWTManager(app)
mongo = PyMongo(app)

@app.route('/api/users/signup', methods=['POST'])
def signup():
    users = mongo.db.users
    first_name = request.get_json()['first_name']
    last_name = request.get_json()['last_name']
    email = request.get_json()['email']
    password = bcrypt.generate_password_hash(request.get_json()['password']).decode('utf-8')
    date_created = datetime.utcnow()

    userObj = users.insert({
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password,
        'date_created': date_created
    })

    checkUser = users.find_one({'__id': userObj})

    result = jsonify({'email': checkUser['email'] + ' registered'})

    return result, status.HTTP_201_CREATED

if __name__ == '__main__':
    app.run(debug=True)
