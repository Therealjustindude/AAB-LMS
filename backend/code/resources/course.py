from flask_restful import Resource


class Courses(Resource):

    def get(self):
        return {'courses': ['java', 'python', 'c++']}