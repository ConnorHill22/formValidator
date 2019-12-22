from flask import Blueprint, jsonify, request
from flask_api import status
from myApp import db, bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from myApp.models import user_model
from myApp._helpers import validators

auth_ctrl = Blueprint('auth', __name__)

validate = validators.preventNoSQLInject
isEmpty = validators.isEmpty

@auth_ctrl.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        user_name = request.get_json()['user_name']
        password = request.get_json()['password']

        # Check if fields are blank
        if( isEmpty(user_name) | isEmpty(password)):
            return jsonify({'msg': 'Error. Please ensure all fields are entered'}), status.HTTP_400_BAD_REQUEST

        # Check if for NoSQL Injects
        if not validate(str, user_name) and not validate(str, password):
            return jsonify({'msg':'Bad Data'}), status.HTTP_400_BAD_REQUEST

        userExists = db.users.find_one({'user_name': user_name})

        if (userExists and bcrypt.check_password_hash(userExists['password'], password)):
            token = user_model.User(userExists).createAccessToken()
            response = jsonify({'msg': 'Success', 'token': token})
            return response, status.HTTP_202_ACCEPTED
        else:
            response = jsonify({'msg': 'Wrong username or password'})
            return response, status.HTTP_401_UNAUTHORIZED


        