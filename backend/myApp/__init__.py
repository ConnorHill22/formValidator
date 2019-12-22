from flask_api import FlaskAPI, status
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_pymongo import PyMongo

from myApp import settings

app = FlaskAPI(__name__)
app.config.from_object(settings)

bcrypt = Bcrypt(app)
jwt = JWTManager(app)
db = PyMongo(app).db

baseUrl = '/api'

from myApp.controllers import user_controller
app.register_blueprint(blueprint=user_controller.user_ctrl, url_prefix= baseUrl + '/users')

from myApp.controllers import auth_controller
app.register_blueprint(blueprint=auth_controller.auth_ctrl, url_prefix= baseUrl + '/auth')