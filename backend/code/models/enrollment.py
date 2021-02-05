# python imports
from sqlalchemy import Column, String, Table, ForeignKey


enrollments = Table(
    'enrollments',
    Column('user_id', String, ForeignKey('users.id')),
    Column('course_id', String, ForeignKey('courses.id'))
)