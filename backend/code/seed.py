# python imports 
import random

# project imports
from app import db, User, Course

# delete and create db
db.drop_all()
db.create_all()


# generate courses
ipsum_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent dolor ipsum, lobortis vel felis et, luctus pellentesque velit. In placerat scelerisque magna, sagittis varius sem. Suspendisse erat nunc, viverra id iaculis eget, tempor in turpis. Pellentesque sed ultricies ipsum. Aenean vitae finibus enim. Aenean malesuada nisl in elit ornare vehicula. Fusce tempor convallis pellentesque. Aliquam sit amet diam purus. Ut vel facilisis quam. Maecenas suscipit commodo scelerisque. Quisque vulputate et lectus quis bibendum. Morbi vestibulum auctor lobortis. Praesent vel eros vel metus molestie finibus eu ac eros. Nam id urna placerat, bibendum orci eget, tempor metus.'
courses = [
    {'id': 1, 'name': 'Java', 'description': ipsum_text},
    {'id': 2, 'name': 'Python', 'description': ipsum_text},
    {'id': 3, 'name': 'C++', 'description': ipsum_text},
    {'id': 4, 'name': 'JavaScript', 'description': ipsum_text},
    {'id': 5, 'name': 'SQL', 'description': ipsum_text}
]

# insert courses
for course in courses:
    course_model = Course(**course)
    db.session.add(course_model)
    db.session.commit()

# generate users
users = [
    {'id': 1, 'name': 'Joely Mcgill'},
    {'id': 2, 'name': 'Hadley Bernard'},
    {'id': 3, 'name': 'Akeel Harrison'},
    {'id': 4, 'name': 'Aisha Shelton'},
    {'id': 5, 'name': 'Harriette Kenny'},
    {'id': 6, 'name': 'Yosef Fitzgerald'},
    {'id': 7, 'name': 'Eloise Ahmed'},
    {'id': 8, 'name': 'Simeon Estes'},
    {'id': 9, 'name': 'Rufus Branch'},
    {'id': 10, 'name': 'Rex Sullivan'}
]

# insert users
course_models = Course.query.all()
for user in users:
    user_model = User(**user)
    number_of_courses = random.randint(1, 3)
    random_indices = random.sample(range(len(course_models)), number_of_courses)
    for index in random_indices:
        random_course = course_models[index]
        user_model.courses.append(random_course)
    db.session.add(user_model)
db.session.commit()
