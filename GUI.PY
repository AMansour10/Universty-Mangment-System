import tkinter as tk
from tkinter import ttk, messagebox
from DB_CONNECTION import DB
import csv
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Set the style for all plots
plt.style.use('seaborn-v0_8-darkgrid')  # Using a valid style name
sns.set_theme(style="darkgrid")  # Setting seaborn theme

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
    def __init__(self, student_id, first_name, last_name, email, department_id):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
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

def add_student(student_id, first_name, last_name, email, department_id):
    # تفعيل خاصية IDENTITY_INSERT للسماح بإدخال قيم للـ ID يدوياً
    DB.run("SET IDENTITY_INSERT Students ON")
    try:
        query = "INSERT INTO Students (StudentID, FirstName, LastName, Email, DepartmentID_FK) VALUES (?, ?, ?, ?, ?)"
        DB.run(query, (student_id, first_name, last_name, email, department_id))
    finally:
        # إعادة تعطيل IDENTITY_INSERT بعد الإضافة
        DB.run("SET IDENTITY_INSERT Students OFF")

def update_student(student_id, first_name, last_name, email, department_id):
    query = "UPDATE Students SET FirstName = ?, LastName = ?, Email = ?, DepartmentID_FK = ? WHERE StudentID = ?"
    DB.run(query, (first_name, last_name, email, department_id, student_id))

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


def fetch_all_data(store_key, tree):
    try:
        if store_key == "departments":
            query = "SELECT DepartmentID, DepartmentName, OfficeLocation FROM Departments"
        elif store_key == "classrooms":
            query = "SELECT RoomID, Building, RoomNumber, Capacity FROM Classrooms"
        elif store_key == "students":
            query = "SELECT StudentID, FirstName, LastName, Email, DepartmentID_FK FROM Students"
        elif store_key == "instructors":
            query = "SELECT InstructorID, FirstName, LastName, Email, DepartmentID_FK FROM Instructors"
        elif store_key == "courses":
            query = "SELECT CourseID, CourseName, Credits, DepartmentID_FK FROM Courses"
        elif store_key == "sections":
            query = "SELECT SectionID, CourseID_FK, InstructorID_FK, RoomID_FK, Semester, Year FROM Sections"
        elif store_key == "enrollments":
            query = "SELECT EnrollmentID, StudentID_FK, SectionID_FK, Grade FROM Enrollments"
        else:
            return

        rows = DB.all(query)
        for row in rows:
            tree.insert('', 'end', values=row)
    except Exception as e:
        messagebox.showerror("خطأ", f"فشل في جلب البيانات: {str(e)}")


# Adding search functionality to the GUI
def search_data(store_key, tree, search_query):
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

        rows = DB.all(query)
        tree.delete(*tree.get_children())  # Clear existing data
        for row in rows:
            tree.insert('', 'end', values=row)
    except Exception as e:
        messagebox.showerror("خطأ", f"فشل في البحث: {str(e)}")

# Adding export functionality to CSV
def export_to_csv(store_key, tree):
    try:
        file_name = f"{store_key}_data.csv"
        with open(file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Write headers
            headers = [tree.heading(col)['text'] for col in tree['columns']]
            writer.writerow(headers)
            # Write data
            for row_id in tree.get_children():
                row = tree.item(row_id, 'values')
                writer.writerow(row)
        messagebox.showinfo("تم", f"تم تصدير البيانات إلى {file_name} بنجاح!")
    except Exception as e:
        messagebox.showerror("خطأ", f"فشل في التصدير: {str(e)}")

# Adding statistics functionality
def show_statistics(store_key):
    try:
        query = ""
        if store_key == "students":
            query = "SELECT DepartmentID_FK, COUNT(*) FROM Students GROUP BY DepartmentID_FK"
        elif store_key == "courses":
            query = "SELECT DepartmentID_FK, COUNT(*) FROM Courses GROUP BY DepartmentID_FK"
        elif store_key == "enrollments":
            query = "SELECT Grade, COUNT(*) FROM Enrollments GROUP BY Grade"

        rows = DB.all(query)
        stats = "\n".join([f"{row[0]}: {row[1]}" for row in rows])
        messagebox.showinfo("إحصائيات", stats)
    except Exception as e:
        messagebox.showerror("خطأ", f"فشل في عرض الإحصائيات: {str(e)}")

# Function to generate a report of students by department
def generate_student_report():
    try:
        query = "SELECT DepartmentID_FK, COUNT(*) FROM Students GROUP BY DepartmentID_FK"
        rows = DB.all(query)
        report = "\n".join([f"Department {row[0]}: {row[1]} students" for row in rows])
        messagebox.showinfo("Student Report", report)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate report: {str(e)}")

# Function to generate a report of courses by instructor
def generate_course_report():
    try:
        query = "SELECT InstructorID_FK, COUNT(*) FROM Sections GROUP BY InstructorID_FK"
        rows = DB.all(query)
        report = "\n".join([f"Instructor {row[0]}: {row[1]} courses" for row in rows])
        messagebox.showinfo("Course Report", report)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate report: {str(e)}")

# Function to show grade chart
def show_grade_chart():
    try:
        # استرجاع البيانات من قاعدة البيانات
        query = "SELECT Grade, COUNT(*) as count FROM Enrollments GROUP BY Grade ORDER BY Grade"
        rows = DB.all(query)
        
        if not rows:
            messagebox.showinfo("تنبيه", "لا توجد بيانات لعرضها")
            return
            
        # إعداد البيانات للرسم البياني
        grades = [str(row[0]) for row in rows]
        counts = [row[1] for row in rows]
        
        # إنشاء نافذة جديدة للرسم البياني
        chart_window = tk.Toplevel()
        chart_window.title("توزيع درجات الطلاب")
        chart_window.geometry("600x400")        # إنشاء الرسم البياني
        fig = Figure(figsize=(10, 6))
        ax = fig.add_subplot(111)
        
        # تحويل البيانات إلى قائمة من النقاط
        import pandas as pd
        df = pd.DataFrame({'Grade': grades, 'Count': counts})        # استخدام Seaborn للرسم بشكل أكثر جمالاً
        sns.set_style("darkgrid", {"grid.color": ".6", "grid.linestyle": ":"})
        barplot = sns.barplot(data=df, x='Grade', y='Count', 
                            color='royalblue', alpha=0.8,
                            ax=ax)
        
        # تخصيص الرسم البياني
        ax.set_title("Student Grades Distribution", fontsize=16, pad=20)
        ax.set_xlabel("Grade", fontsize=14, labelpad=10)
        ax.set_ylabel("Number of Students", fontsize=14, labelpad=10)
        
        # تحسين شكل الأعمدة
        for container in ax.containers:
            ax.bar_label(container, padding=5)
        
        # تحسين مظهر المحاور
        ax.tick_params(axis='both', which='major', labelsize=12)
          # إضافة القيم فوق الأعمدة مع خلفية
        for x, y in zip(df['Grade'], df['Count']):
            ax.text(x, y + max(counts) * 0.03, str(int(y)),
                   ha='center', va='bottom',
                   fontsize=11, fontweight='bold',
                   bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))
        
        # تحسين المظهر العام
        sns.despine(left=True, bottom=True)  # إزالة الإطار
        ax.grid(True, linestyle='--', alpha=0.7)  # تحسين شبكة الخلفية
        
        # عرض الرسم البياني في النافذة
        canvas = FigureCanvasTkAgg(fig, master=chart_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
    except Exception as e:
        messagebox.showerror("خطأ", f"حدث خطأ أثناء إنشاء الرسم البياني: {str(e)}")

root = tk.Tk()
root.title("نظام إدارة الجامعة")
root.geometry("900x600")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)


def create_form(frame, fields, submit_callback):
    entries = {}
    for i, (label, key) in enumerate(fields):
        tk.Label(frame, text=label).grid(row=i, column=0, padx=5, pady=5)
        entry = tk.Entry(frame)
        entry.grid(row=i, column=1, padx=5, pady=5)
        entries[key] = entry
    return entries

def create_table(frame, columns):
    tree = ttk.Treeview(frame, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    tree.pack(fill="both", expand=True, pady=10)
    return tree


data_store = {
    "departments": [],
    "classrooms": [],
    "students": [],
    "instructors": [],
    "courses": [],
    "sections": [],
    "enrollments": []
}

def add_to_list_and_tree(obj, store_key, tree, values):
    data_store[store_key].append(obj)
    tree.insert('', 'end', values=values)

def create_tab(name, fields, store_key, class_type, columns, extract_values):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=name)
    form_frame = tk.LabelFrame(frame, text="إدخال البيانات")
    form_frame.pack(fill="x", padx=10, pady=5)
    table_frame = tk.LabelFrame(frame, text="العناصر المُضافة")
    table_frame.pack(fill="both", expand=True, padx=10, pady=5)

    def submit(entries):
        try:
            values = [entries[k].get() for _, k in fields]
            obj = class_type(*values)
            
            # محاولة إضافة البيانات في قاعدة البيانات أولاً
            if store_key == "departments":
                add_department(*values)
            elif store_key == "classrooms":
                add_classroom(*values)
            elif store_key == "students":
                add_student(*values)
            elif store_key == "instructors":
                add_instructor(*values)
            elif store_key == "courses":
                add_course(*values)
            elif store_key == "sections":
                add_section(*values)
            elif store_key == "enrollments":
                add_enrollment(*values)
                
            # إذا نجحت الإضافة في قاعدة البيانات، نضيف في الواجهة
            add_to_list_and_tree(obj, store_key, tree, extract_values(obj))
            
            # مسح الحقول بعد الإضافة الناجحة
            for e in entries.values():
                e.delete(0, tk.END)
            messagebox.showinfo("تم", f"تمت إضافة {name} بنجاح!")
            
        except Exception as e:
            messagebox.showerror("خطأ", f"فشل في إضافة البيانات: {str(e)}")

    def delete_selected():
        try:
            selected_item = tree.selection()[0]
            values = tree.item(selected_item, 'values')
            # Ensure ID is cleaned and converted to integer
            cleaned_id = int(str(values[0]).strip().replace("'", ""))
            if store_key == "departments":
                delete_department(cleaned_id)
            elif store_key == "classrooms":
                delete_classroom(cleaned_id)
            elif store_key == "students":
                delete_student(cleaned_id)
            elif store_key == "instructors":
                delete_instructor(cleaned_id)
            elif store_key == "courses":
                delete_course(cleaned_id)
            elif store_key == "sections":
                delete_section(cleaned_id)
            elif store_key == "enrollments":
                delete_enrollment(cleaned_id)
            tree.delete(selected_item)
            messagebox.showinfo("تم", f"تم حذف {name} بنجاح!")
        except Exception as e:
            messagebox.showerror("خطأ", f"فشل في الحذف: {str(e)}")

    def update_selected(entries):
        try:
            selected_item = tree.selection()[0]
            values = [entries[k].get() for _, k in fields]
            if store_key == "departments":
                update_department(*values)
            elif store_key == "classrooms":
                update_classroom(*values)
            elif store_key == "students":
                update_student(*values)
            elif store_key == "instructors":
                update_instructor(*values)
            elif store_key == "courses":
                update_course(*values)
            elif store_key == "sections":
                update_section(*values)
            elif store_key == "enrollments":
                update_enrollment(*values)
            tree.item(selected_item, values=values)
            messagebox.showinfo("تم", f"تم تحديث {name} بنجاح!")
        except Exception as e:
            messagebox.showerror("خطأ", str(e))

    entries = create_form(form_frame, fields, submit)
    tree = create_table(table_frame, columns)

    # Fetch and display all data when the tab is created
    fetch_all_data(store_key, tree)

    button_frame = tk.Frame(form_frame)
    button_frame.grid(row=len(fields), column=0, columnspan=2, pady=10)

    submit_btn = tk.Button(button_frame, text="إضافة", command=lambda: submit(entries))
    submit_btn.pack(side="left", padx=5)

    update_btn = tk.Button(button_frame, text="تحديث", command=lambda: update_selected(entries))
    update_btn.pack(side="left", padx=5)

    delete_btn = tk.Button(button_frame, text="حذف", command=delete_selected)
    delete_btn.pack(side="left", padx=5)

    search_entry = tk.Entry(form_frame)
    search_entry.grid(row=len(fields) + 1, column=0, padx=5, pady=5)
    search_btn = tk.Button(form_frame, text="بحث", command=lambda: search_data(store_key, tree, search_entry.get()))
    search_btn.grid(row=len(fields) + 1, column=1, padx=5, pady=5)

    export_btn = tk.Button(button_frame, text="تصدير", command=lambda: export_to_csv(store_key, tree))
    export_btn.pack(side="left", padx=5)

    stats_btn = tk.Button(button_frame, text="إحصائيات", command=lambda: show_statistics(store_key))
    stats_btn.pack(side="left", padx=5)

    # Adding a frame for report buttons
    report_frame = tk.Frame(frame, bg="lightblue")
    report_frame.pack(fill="x", padx=10, pady=5)

    if store_key == "students":
        report_btn = tk.Button(report_frame, text="Generate Student Report", command=generate_student_report)
        report_btn.pack(side="left", padx=5, pady=5)
    elif store_key == "courses":
        report_btn = tk.Button(report_frame, text="Generate Course Report", command=generate_course_report)
        report_btn.pack(side="left", padx=5, pady=5)
    elif store_key == "enrollments":
        chart_btn = tk.Button(report_frame, text="عرض الرسم البياني للدرجات", command=show_grade_chart)
        chart_btn.pack(side="left", padx=5, pady=5)


create_tab("Department", [("ID", "id"), ("Name", "name"), ("Office", "office")], 
           "departments", Department, ["ID", "Name", "Office"], 
           lambda d: (d.department_id, d.name, d.office_location))

create_tab("Classroom", [("ID", "id"), ("Building", "building"), ("Room Number", "room"), ("Capacity", "capacity")], 
           "classrooms", Classroom, ["ID", "Building", "Room", "Capacity"], 
           lambda c: (c.room_id, c.building, c.room_number, c.capacity))

create_tab("Student", [("ID", "id"), ("First Name", "fname"), ("Last Name", "lname"), 
                       ("Email", "email"), ("Department ID", "dept_id")],
           "students", Student, ["ID", "First", "Last", "Email", "Dept"], 
           lambda s: (s.student_id, s.first_name, s.last_name, s.email, s.department_id))

create_tab("Instructor", [("ID", "id"), ("First Name", "fname"), ("Last Name", "lname"), 
                          ("Email", "email"), ("Department ID", "dept_id")],
           "instructors", Instructor, ["ID", "First", "Last", "Email", "Dept"], 
           lambda i: (i.instructor_id, i.first_name, i.last_name, i.email, i.department_id))

create_tab("Course", [("ID", "id"), ("Name", "name"), ("Credits", "credits"), ("Department ID", "dept_id")],
           "courses", Course, ["ID", "Name", "Credits", "Dept"], 
           lambda c: (c.course_id, c.course_name, c.credits, c.department_id))

create_tab("Section", [("ID", "id"), ("Course ID", "course_id"), ("Instructor ID", "instructor_id"), 
                       ("Room ID", "room_id"), ("Semester", "semester"), ("Year", "year")],
           "sections", Section, ["ID", "Course", "Instructor", "Room", "Sem", "Year"], 
           lambda s: (s.section_id, s.course_id, s.instructor_id, s.room_id, s.semester, s.year))

create_tab("Enrollment", [("ID", "id"), ("Student ID", "student_id"), ("Section ID", "section_id"), ("Grade", "grade")],
           "enrollments", Enrollment, ["ID", "Student", "Section", "Grade"], 
           lambda e: (e.enrollment_id, e.student_id, e.section_id, e.grade))

root.mainloop()
