# project imports
from models.base import BaseModel

class CourseModel(BaseModel, db.Model):
    '''
    Course
    '''

    course = Column(String, nullable=False)