#### IMPORTS

## python imports
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

## project imports
from db import db

from resources.course import Courses
from resources.user import Users, User
from seed import users as seed_users, courses as seed_courses
from models.user import UserModel
from models.course import CourseModel
import random

#### APP CONFIG

# initialize
app = Flask(__name__)
# connect db to app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# enable cross resource sharing
CORS(app)

# connect flask_restful to app
api = Api(app)

# create db if DNE before first request is run
# SQLAlchemy can only create tables it sees (it sees tables because we import the resource which imports the model)
# we can also import models directly and db will create
# ex. import Courses resource <= Courses imports CourseModel <= CourseModel has tablename
@app.before_first_request
def create_tables():
    db.create_all()


#### ENDPOINT CONFIG

@app.route('/')
def index():
    users = [UserModel(**user) for user in seed_users]
    courses = [CourseModel(**course) for course in seed_courses]
    [UserModel(**user).save_to_db() for user in seed_users]
    #[CourseModel(**course).save_to_db() for course in seed_courses]
    for course in courses:
        course_user_ids = [user.id for user in course.users]
        number_of_students = random.randint(1, 5)
        for i in range(number_of_students):
            random_index = random.randint(0, len(users)-1)
            random_student = users[random_index]
            if random_student.id not in course_user_ids:
                course.users.append(random_student)
        course.save_to_db()
    return "Hello World"

api.add_resource(Courses, '/backend/courses')
api.add_resource(User, '/backend/users/<string:id>')
api.add_resource(Users, '/backend/users')


# RUN APP
if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True)