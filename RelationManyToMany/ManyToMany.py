from peewee import *
from playhouse.fields import ManyToManyField

db = SqliteDatabase('school.db')


class BaseModel(Model):
    class Meta:
        database = db


class Student(BaseModel):
    name = CharField()


class Course(BaseModel):
    name = CharField()
    students = ManyToManyField(Student, related_name='courses')


StudentCourse = Course.students.get_through_model()

db.create_tables([
    Student,
    Course,
    StudentCourse])

std = Student.get(Student.name == 'Huey')
for course in std.courses.order_by(Course.name):
    print(course.name)

engl = Course.get(Course.name == 'English')
for student in engl.students:
    print(student.name)
