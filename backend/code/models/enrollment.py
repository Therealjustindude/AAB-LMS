# project imports
from db import db

enrollments = db.Table(
    'enrollments',
    db.Column('user_id', db.String, db.ForeignKey('users.id')),
    db.Column('course_id', db.String, db.ForeignKey('courses.id'))
)