from models.course import CourseModel
from models.user import UserModel

users = [
    {'first_name': 'Joely', 'last_name': 'Mcgill'},
    {'first_name': 'Hadley', 'last_name': 'Bernard'},
    {'first_name': 'Akeel', 'last_name': 'Harrison'},
    {'first_name': 'Aisha', 'last_name': 'Shelton'},
    {'first_name': 'Harriette', 'last_name': 'Kenny'},
    {'first_name': 'Yosef', 'last_name': 'Fitzgerald'},
    {'first_name': 'Eloise', 'last_name': 'Ahmed'},
    {'first_name': 'Simeon', 'last_name': 'Estes'},
    {'first_name': 'Rufus', 'last_name': 'Branch'},
    {'first_name': 'Rex', 'last_name': 'Sullivan'}
]
for user in users:
    user['email'] = f"{user['first_name'].lower()}@{user['last_name'].lower()}.com"
    user['password'] = 'password'
    #user_model = UserModel(**user)
    #user_model.save_to_db()


courses = [
    {
        'course': 'Java'
    },
    {
        'course': 'Python'
    },
    {
        'course': 'C++'
    },
    {
        'course': 'JavaScript'
    }
]
#for course in courses:
#    course_model = CourseModel(**course)
    #course_model.save_to_db()
    