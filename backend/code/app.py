#### IMPORTS

## python imports
from flask import Flask
from flask_restful import Api

## project imports
from resources.course import Courses

#### APP CONFIG

# initialize
app = Flask(__name__)
# connect flask_restful to app
api = Api(app)


#### ENDPOINT CONFIG

@app.route('/')
def index():
    return "Hello World"

api.add_resource(Courses, '/backend/courses')


# RUN APP
if __name__ == "__main__":
    app.run(debug=True)