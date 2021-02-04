# python imports
from sqlalchemy import Column, String

# project imports
from db import db
from models.base import BaseModel

class CourseModel(BaseModel, db.Model):
    '''
    Course
    '''

    __tablename__ = 'courses' 

    course = Column(
                String, 
                nullable=False
    )

    # method to return dictionary version
    def json(self):
        return {
                'id': course.id, 
                'course': course.course
            }
