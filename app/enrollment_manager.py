"""
enrollment_manager.py
----------------------
Links students to courses. This is the third required functional
module, and it's the one that makes the system relational rather
than two independent lists: it validates that both the student and
the course actually exist before creating an enrollment.
"""

import os
import uuid
from app import storage, utils, student_manager, course_manager

FIELDNAMES = ["enrollment_id", "student_id", "course_id", "grade"]
DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "enrollments.csv")


def enroll_student(student_id, course_id):
    if not student_manager.find_student(student_id):
        return False, f"No such student '{student_id}'."
    if not course_manager.find_course(course_id):
        return False, f"No such course '{course_id}'."

    enrollments = storage.read_all(DATA_FILE, FIELDNAMES)
    if any(e["student_id"] == student_id and e["course_id"] == course_id for e in enrollments):
        return False, "Student is already enrolled in this course."

    enrollment_id = uuid.uuid4().hex[:8]
    storage.append_row(DATA_FILE, FIELDNAMES, {
        "enrollment_id": enrollment_id, "student_id": student_id,
        "course_id": course_id, "grade": ""
    })
    utils.log_action(f"Enrolled student {student_id} in course {course_id}")
    return True, f"Enrolled successfully (enrollment ID: {enrollment_id})."


def drop_enrollment(enrollment_id):
    enrollments = storage.read_all(DATA_FILE, FIELDNAMES)
    remaining = [e for e in enrollments if e["enrollment_id"] != enrollment_id]
    if len(remaining) == len(enrollments):
        return False, f"Enrollment '{enrollment_id}' not found."
    storage.write_all(DATA_FILE, FIELDNAMES, remaining)
    utils.log_action(f"Dropped enrollment {enrollment_id}")
    return True, "Enrollment dropped."


def set_grade(enrollment_id, grade):
    enrollments = storage.read_all(DATA_FILE, FIELDNAMES)
    found = False
    for e in enrollments:
        if e["enrollment_id"] == enrollment_id:
            e["grade"] = grade
            found = True
    if not found:
        return False, f"Enrollment '{enrollment_id}' not found."
    storage.write_all(DATA_FILE, FIELDNAMES, enrollments)
    utils.log_action(f"Set grade for enrollment {enrollment_id} to {grade}")
    return True, "Grade updated."


def view_enrollments():
    return storage.read_all(DATA_FILE, FIELDNAMES)
