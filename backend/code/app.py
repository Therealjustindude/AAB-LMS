#### IMPORTS

## python imports
from flask import Flask
from flask_restful import Api

## project imports
from db import db
from models.course import CourseModel
from resources.course import Courses

#### APP CONFIG

# initialize
app = Flask(__name__)
# connect db to app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
    return "Hello World"

api.add_resource(Courses, '/backend/courses')


# RUN APP
if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True)