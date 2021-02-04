# python imports
from sqlalchemy import Column, String

# project imports
from db import db
from models.base import BaseMixin

class CourseModel(BaseMixin, db.Model):
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
                'id': self.id, 
                'course': self.course
            }
