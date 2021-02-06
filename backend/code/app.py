#### IMPORTS

## python imports
from flask import Flask, request
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

enrollments = db.Table(
    'enrollments',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True)
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    courses = db.relationship('Course', secondary=enrollments, lazy='subquery',
        backref=db.backref('users', lazy=True))

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

@app.route('/backend/courses/<int:course_id>')
def get_course(course_id):
    course = Course.query.filter_by(id=course_id).first()
    return course.to_json()

@app.route('/backend/courses/<int:course_id>/users')
def get_course_users(course_id):
    course = Course.query.filter_by(id=course_id).first()
    return {'users': [user.to_json() for user in course.users]}

@app.route('/backend/users')
def list_users():
    return {'users': [user.to_json() for user in User.query.all()]}

@app.route('/backend/users/<int:user_id>')
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    return user.to_json()

@app.route('/backend/users/<int:user_id>/courses')
def get_user_courses(user_id):
    user = User.query.filter_by(id=user_id).first()
    return {'courses': [course.to_json() for course in user.courses]}

@app.route('/backend/users/<int:user_id>/courses/<int:course_id>', methods=['GET', 'POST', 'DELETE'])
def get_user_course(user_id, course_id):
    user = User.query.filter_by(id=user_id).first()
    course = Course.query.filter_by(id=course_id).first()
    
    if request.method == 'GET':
        return get_course(course_id)

    if request.method == 'POST':
        user.courses.append(course)
        db.session.commit()
    
    elif request.method == 'DELETE':
        user.courses.remove(course)
        db.session.commit()

    return get_user_courses(user_id)

if __name__ == "__main__":
    app.run(debug=True)
