# python imports
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref

# project imports
from db import db
from models.base import BaseMixin
from models.enrollment import enrollments

class UserModel(BaseMixin, db.Model):
    '''
    User
    '''

    __tablename__ = 'users' 

    first_name = Column(
                String, 
                nullable=False
    )
    last_name = Column(
                String, 
                nullable=False
    )
    email = Column(
                String, 
                nullable=False,
                unique=True
    )
    password = Column(
                String, 
                nullable=False
    )
    courses = relationship(
                    'CourseModel',
                    secondary=enrollments,
                    backref=backref(
                                    'users',
                                    lazy='dynamic'
                    )
    )

    # method to return dictionary version
    def json(self):
        return {
                'id': self.id, 
                'first name': self.first_name,
                'last_name': self.last_name,
                'email': self.email
            }
