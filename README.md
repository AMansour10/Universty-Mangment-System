# 🎓 University Management System

A comprehensive **University Management System** that provides functionalities to manage departments, classrooms, students, instructors, courses, and enrollments.  
It uses a **SQL Server database** for storing and retrieving data and provides a **Graphical User Interface (GUI)** for interaction.

---

## 📂 Project Structure

### Files and Directories
- **`DB_CONNECTION.py`** → Handles database connection and provides methods to execute queries.  
- **`GUI.PY`** → Implements the GUI using `tkinter`, integrates data visualization with `matplotlib` and `seaborn`.  
- **`models.py`** → Defines data models for university entities (`Department`, `Classroom`, `Student`, `Instructor`, `Course`, `Section`, `Enrollment`).  
- **`operations.py`** → Contains functions to perform CRUD operations on database entities.  
- **`classrooms_data.csv`** → Sample dataset of classrooms.  
- **`departments_data.csv`** → Sample dataset of departments.  

---

## 🚀 Features

### 1. Database Connection
- **File**: `DB_CONNECTION.py`
- Uses `pyodbc` to connect to SQL Server.
- Provides helper methods:
  - `run` → Run queries.  
  - `all` → Fetch all results.  
  - `one` → Fetch a single result.  
  - `close` → Close the connection.  

### 2. Graphical User Interface
- **File**: `GUI.PY`
- Built with `tkinter`.  
- Data visualization using **matplotlib** and **seaborn**.  
- User-friendly interface for managing university data.  

### 3. Data Models
- **File**: `models.py`  
- Classes represent university entities:
  - `Department`  
  - `Classroom`  
  - `Student`  
  - `Instructor`  
  - `Course`  
  - `Section`  
  - `Enrollment`  

### 4. CRUD Operations
- **File**: `operations.py`  
- Functions to:
  - Add new records.  
  - Update existing records.  
  - Delete records.  
- Supported entities: Departments, Classrooms, Students, Instructors.  

---

## 📦 Requirements

Install the following Python libraries before running:

```bash
pip install pyodbc matplotlib seaborn
