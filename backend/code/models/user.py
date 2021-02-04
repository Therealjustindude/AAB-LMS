# python imports
from sqlalchemy import Column, String

# project imports
from db import db
from models.base import BaseMixin

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

    # method to return dictionary version
    def json(self):
        return {
                'id': self.id, 
                'first name': self.first_name,
                'last_name': self.last_name,
                'email': self.email
            }
