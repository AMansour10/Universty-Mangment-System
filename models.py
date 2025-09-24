class Department:
    def __init__(self, department_id, name, office_location):
        self.department_id = department_id
        self.name = name
        self.office_location = office_location

class Classroom:
    def __init__(self, room_id, building, room_number, capacity):
        self.room_id = room_id
        self.building = building
        self.room_number = room_number
        self.capacity = capacity

class Student:
    def __init__(self, student_id, first_name, last_name, date_of_birth, email, department_id):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.department_id = department_id

class Instructor:
    def __init__(self, instructor_id, first_name, last_name, email, department_id):
        self.instructor_id = instructor_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.department_id = department_id

class Course:
    def __init__(self, course_id, course_name, credits, department_id):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits
        self.department_id = department_id

class Section:
    def __init__(self, section_id, course_id, instructor_id, room_id, semester, year):
        self.section_id = section_id
        self.course_id = course_id
        self.instructor_id = instructor_id
        self.room_id = room_id
        self.semester = semester
        self.year = year

class Enrollment:
    def __init__(self, enrollment_id, student_id, section_id, grade):
        self.enrollment_id = enrollment_id
        self.student_id = student_id
        self.section_id = section_id
        self.grade = grade
