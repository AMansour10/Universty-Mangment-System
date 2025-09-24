from DB_CONNECTION import DB

def add_department(department_id, name, office_location):
    query = "INSERT INTO Departments (DepartmentID, DepartmentName, OfficeLocation) VALUES (?, ?, ?)"
    DB.run(query, (department_id, name, office_location))

def update_department(department_id, name, office_location):
    query = "UPDATE Departments SET DepartmentName = ?, OfficeLocation = ? WHERE DepartmentID = ?"
    DB.run(query, (name, office_location, department_id))

def delete_department(department_id):
    query = "DELETE FROM Departments WHERE DepartmentID = ?"
    DB.run(query, (department_id,))

def add_classroom(room_id, building, room_number, capacity):
    query = "INSERT INTO Classrooms (RoomID, Building, RoomNumber, Capacity) VALUES (?, ?, ?, ?)"
    DB.run(query, (room_id, building, room_number, capacity))

def update_classroom(room_id, building, room_number, capacity):
    query = "UPDATE Classrooms SET Building = ?, RoomNumber = ?, Capacity = ? WHERE RoomID = ?"
    DB.run(query, (building, room_number, capacity, room_id))

def delete_classroom(room_id):
    query = "DELETE FROM Classrooms WHERE RoomID = ?"
    DB.run(query, (room_id,))

def add_student(student_id, first_name, last_name, date_of_birth, email, department_id):
    query = "INSERT INTO Students (StudentID, FirstName, LastName, DateOfBirth, Email, DepartmentID_FK) VALUES (?, ?, ?, ?, ?, ?)"
    DB.run(query, (student_id, first_name, last_name, date_of_birth, email, department_id))

def update_student(student_id, first_name, last_name, date_of_birth, email, department_id):
    query = "UPDATE Students SET FirstName = ?, LastName = ?, DateOfBirth = ?, Email = ?, DepartmentID_FK = ? WHERE StudentID = ?"
    DB.run(query, (first_name, last_name, date_of_birth, email, department_id, student_id))

def delete_student(student_id):
    query = "DELETE FROM Students WHERE StudentID = ?"
    DB.run(query, (student_id,))

def add_instructor(instructor_id, first_name, last_name, email, department_id):
    query = "INSERT INTO Instructors (InstructorID, FirstName, LastName, Email, DepartmentID_FK) VALUES (?, ?, ?, ?, ?)"
    DB.run(query, (instructor_id, first_name, last_name, email, department_id))

def update_instructor(instructor_id, first_name, last_name, email, department_id):
    query = "UPDATE Instructors SET FirstName = ?, LastName = ?, Email = ?, DepartmentID_FK = ? WHERE InstructorID = ?"
    DB.run(query, (first_name, last_name, email, department_id, instructor_id))

def delete_instructor(instructor_id):
    query = "DELETE FROM Instructors WHERE InstructorID = ?"
    DB.run(query, (instructor_id,))

def add_course(course_id, course_name, credits, department_id):
    query = "INSERT INTO Courses (CourseID, CourseName, Credits, DepartmentID_FK) VALUES (?, ?, ?, ?)"
    DB.run(query, (course_id, course_name, credits, department_id))

def update_course(course_id, course_name, credits, department_id):
    query = "UPDATE Courses SET CourseName = ?, Credits = ?, DepartmentID_FK = ? WHERE CourseID = ?"
    DB.run(query, (course_name, credits, department_id, course_id))

def delete_course(course_id):
    query = "DELETE FROM Courses WHERE CourseID = ?"
    DB.run(query, (course_id,))

def add_section(section_id, course_id, instructor_id, room_id, semester, year):
    query = "INSERT INTO Sections (SectionID, CourseID_FK, InstructorID_FK, RoomID_FK, Semester, Year) VALUES (?, ?, ?, ?, ?, ?)"
    DB.run(query, (section_id, course_id, instructor_id, room_id, semester, year))

def update_section(section_id, course_id, instructor_id, room_id, semester, year):
    query = "UPDATE Sections SET CourseID_FK = ?, InstructorID_FK = ?, RoomID_FK = ?, Semester = ?, Year = ? WHERE SectionID = ?"
    DB.run(query, (course_id, instructor_id, room_id, semester, year, section_id))

def delete_section(section_id):
    query = "DELETE FROM Sections WHERE SectionID = ?"
    DB.run(query, (section_id,))

def add_enrollment(enrollment_id, student_id, section_id, grade):
    query = "INSERT INTO Enrollments (EnrollmentID, StudentID_FK, SectionID_FK, Grade) VALUES (?, ?, ?, ?)"
    DB.run(query, (enrollment_id, student_id, section_id, grade))

def update_enrollment(enrollment_id, student_id, section_id, grade):
    query = "UPDATE Enrollments SET StudentID_FK = ?, SectionID_FK = ?, Grade = ? WHERE EnrollmentID = ?"
    DB.run(query, (student_id, section_id, grade, enrollment_id))

def delete_enrollment(enrollment_id):
    query = "DELETE FROM Enrollments WHERE EnrollmentID = ?"
    DB.run(query, (enrollment_id,))

def fetch_all_data(store_key):
    try:
        if store_key == "departments":
            query = "SELECT DepartmentID, DepartmentName, OfficeLocation FROM Departments"
        elif store_key == "classrooms":
            query = "SELECT RoomID, Building, RoomNumber, Capacity FROM Classrooms"
        elif store_key == "students":
            query = "SELECT StudentID, FirstName, LastName, DateOfBirth, Email, DepartmentID_FK FROM Students"
        elif store_key == "instructors":
            query = "SELECT InstructorID, FirstName, LastName, Email, DepartmentID_FK FROM Instructors"
        elif store_key == "courses":
            query = "SELECT CourseID, CourseName, Credits, DepartmentID_FK FROM Courses"
        elif store_key == "sections":
            query = "SELECT SectionID, CourseID_FK, InstructorID_FK, RoomID_FK, Semester, Year FROM Sections"
        elif store_key == "enrollments":
            query = "SELECT EnrollmentID, StudentID_FK, SectionID_FK, Grade FROM Enrollments"
        else:
            return None

        return DB.all(query)
    except Exception as e:
        raise Exception(f"فشل في جلب البيانات: {str(e)}")

def search_data(store_key, search_query):
    try:
        query = ""
        if store_key == "departments":
            query = f"SELECT * FROM Departments WHERE DepartmentName LIKE '%{search_query}%'"
        elif store_key == "classrooms":
            query = f"SELECT * FROM Classrooms WHERE Building LIKE '%{search_query}%'"
        elif store_key == "students":
            query = f"SELECT * FROM Students WHERE FirstName LIKE '%{search_query}%' OR LastName LIKE '%{search_query}%'"
        elif store_key == "instructors":
            query = f"SELECT * FROM Instructors WHERE FirstName LIKE '%{search_query}%' OR LastName LIKE '%{search_query}%'"
        elif store_key == "courses":
            query = f"SELECT * FROM Courses WHERE CourseName LIKE '%{search_query}%'"
        elif store_key == "sections":
            query = f"SELECT * FROM Sections WHERE Semester LIKE '%{search_query}%'"
        elif store_key == "enrollments":
            query = f"SELECT * FROM Enrollments WHERE Grade LIKE '%{search_query}%'"

        return DB.all(query)
    except Exception as e:
        raise Exception(f"فشل في البحث: {str(e)}")
