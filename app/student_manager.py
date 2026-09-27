"""
student_manager.py
-------------------
All operations for the "Student" entity: add, view, update, delete.
This is one of the three required functional modules.
"""

import os
from app import storage, utils

FIELDNAMES = ["student_id", "name", "email", "department"]
DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "students.csv")


def add_student(student_id, name, email, department):
    if not utils.is_non_empty(student_id) or not utils.is_non_empty(name):
        return False, "Student ID and name are required."
    if not utils.is_valid_email(email):
        return False, "Invalid email format."

    students = storage.read_all(DATA_FILE, FIELDNAMES)
    if any(s["student_id"] == student_id for s in students):
        return False, f"Student ID '{student_id}' already exists."

    storage.append_row(DATA_FILE, FIELDNAMES, {
        "student_id": student_id, "name": name, "email": email, "department": department
    })
    utils.log_action(f"Added student {student_id} ({name})")
    return True, "Student added successfully."


def view_students():
    return storage.read_all(DATA_FILE, FIELDNAMES)


def find_student(student_id):
    students = storage.read_all(DATA_FILE, FIELDNAMES)
    for s in students:
        if s["student_id"] == student_id:
            return s
    return None


def update_student(student_id, **fields):
    students = storage.read_all(DATA_FILE, FIELDNAMES)
    found = False
    for s in students:
        if s["student_id"] == student_id:
            for key, value in fields.items():
                if value:
                    s[key] = value
            found = True
    if not found:
        return False, f"Student '{student_id}' not found."
    storage.write_all(DATA_FILE, FIELDNAMES, students)
    utils.log_action(f"Updated student {student_id}")
    return True, "Student updated successfully."


def delete_student(student_id):
    students = storage.read_all(DATA_FILE, FIELDNAMES)
    remaining = [s for s in students if s["student_id"] != student_id]
    if len(remaining) == len(students):
        return False, f"Student '{student_id}' not found."
    storage.write_all(DATA_FILE, FIELDNAMES, remaining)
    utils.log_action(f"Deleted student {student_id}")
    return True, "Student deleted successfully."
