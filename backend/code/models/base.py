# python imports
from sqlalchemy import Column, String
from uuid import uuid4

# project imports
from db import db


class BaseModel(object):
    '''
    Base model - will be inherited by all other models
    '''

    # primary key column - value will be generated on record creation
    id = Column(
            String, 
            primary_key=True, 
            default=lambda: str(uuid4())
    )

    # method to upsert record (inserts into database if not exists or updates in database)
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # method to delete record from database
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

