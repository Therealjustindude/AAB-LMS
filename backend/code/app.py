#### IMPORTS

## python imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS



#### APP CONFIG

# initialize
app = Flask(__name__)
# connect db to app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# enable cross resource sharing
CORS(app)


#### MODEL CONFIG

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def to_json(self):
        return {
            'id': self.id, 
            'name': self.name
        }

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }


#### ROUTE CONFIG

@app.route('/')
def index():
    return "Hello World"

@app.route('/backend/courses')
def list_courses():
    return {'courses': [course.to_json() for course in Course.query.all()]}

@app.route('/backend/users')
def list_users():
    return {'users': [user.to_json() for user in User.query.all()]}

if __name__ == "__main__":
    app.run(debug=True)






# create db if DNE before first request is run
# SQLAlchemy can only create tables it sees (it sees tables because we import the resource which imports the model)
# we can also import models directly and db will create
# ex. import Courses resource <= Courses imports CourseModel <= CourseModel has tablename
#@app.before_first_request
#def create_tables():
#    db.create_all()


##### ENDPOINT CONFIG

#@app.route('/')
#def index():
#    users = [UserModel(**user) for user in seed_users]
#    courses = [CourseModel(**course) for course in seed_courses]
#    [UserModel(**user).save_to_db() for user in seed_users]
#    #[CourseModel(**course).save_to_db() for course in seed_courses]
#    for course in courses:
#        course_user_ids = [user.id for user in course.users]
#        number_of_students = random.randint(1, 5)
#        for i in range(number_of_students):
#            random_index = random.randint(0, len(users)-1)
#            random_student = users[random_index]
#            if random_student.id not in course_user_ids:
#                course.users.append(random_student)
#        course.save_to_db()
#    return "Hello World"

#api.add_resource(Courses, '/backend/courses')
#api.add_resource(User, '/backend/users/<string:id>')
#api.add_resource(Users, '/backend/users')


## RUN APP
#if __name__ == "__main__":
#    db.init_app(app)
#    app.run(debug=True)