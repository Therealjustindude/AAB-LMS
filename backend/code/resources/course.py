# python imports
from flask_restful import Resource

# project imports
from models.course import CourseModel


class Courses(Resource):

    def get(self):
        return {'courses': [course.json() for course in CourseModel.query.all()]}