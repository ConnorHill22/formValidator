from flask import Blueprint, jsonify, request
from flask_api import status
from myApp import db
from myApp.models import user_model
from myApp._helpers import validators

user_ctrl = Blueprint('user', __name__)

validate = validators.preventNoSQLInject
isEmpty = validators.isEmpty

@user_ctrl.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        userObj = {
            'user_name': request.get_json()['user_name'],
            'first_name': request.get_json()['first_name'],
            'last_name': request.get_json()['last_name'],
            'password': request.get_json()['password'],
            'email': request.get_json()['email']
        }

        # Check if Empty
        if( isEmpty(userObj['user_name']) | isEmpty(userObj['first_name']) | isEmpty(userObj['last_name']) | isEmpty(userObj['password']) | isEmpty(userObj['email'])):
            return jsonify({'msg': 'Error. Please ensure all fields are entered'}), status.HTTP_400_BAD_REQUEST
        # Check for injections
        if not (validate(str, userObj['user_name']) & validate(str, userObj['first_name']) & validate(str, userObj['last_name']) & validate(str, userObj['password']) & validate(str, userObj['email'])):
            return jsonify({'msg':'Bad Data'}), status.HTTP_400_BAD_REQUEST

        # Data is cleaned
        # See if the username already exists, if so return error
        userExists = db.users.find_one({"user_name": userObj['user_name']})
        if not userExists:  
            user = user_model.User(userObj)
            user_id = user.save()
            response = jsonify({'msg': db.users.find_one({"_id": user_id})['user_name'] + ' registered'})
            return response, status.HTTP_201_CREATED
        else:
            return jsonify({'msg': "Username is taken"}), status.HTTP_400_BAD_REQUEST