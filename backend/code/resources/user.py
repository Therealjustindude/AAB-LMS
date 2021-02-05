# python imports
from flask_restful import Resource

# project imports
from models.user import UserModel


class User(Resource):
    
    def get(self, id):
        user = UserModel.query.get(id)
        if user:
            return user.json()
        return {'message': 'User not found'}, 404

class Users(Resource):

    def get(self):
        return {'users': [user.json() for user in UserModel.query.all()]}