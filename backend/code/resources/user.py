# python imports
from flask_restful import Resource

# project imports
from models.user import UserModel


class Users(Resource):

    def get(self):
        return {'users': [user.json() for user in UserModel.query.all()]}