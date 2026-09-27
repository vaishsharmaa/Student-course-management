"""
models.py
---------
Plain data classes describing the three core entities in the system.
Keeping these separate from the "manager" modules means the shape of
our data lives in exactly one place.
"""

from dataclasses import dataclass


@dataclass
class Student:
    student_id: str
    name: str
    email: str
    department: str

    def to_row(self):
        """Convert to a list, ready for writing to CSV."""
        return [self.student_id, self.name, self.email, self.department]


@dataclass
class Course:
    course_id: str
    course_name: str
    credits: str
    instructor: str

    def to_row(self):
        return [self.course_id, self.course_name, self.credits, self.instructor]


@dataclass
class Enrollment:
    enrollment_id: str
    student_id: str
    course_id: str
    grade: str  # empty string if not graded yet

    def to_row(self):
        return [self.enrollment_id, self.student_id, self.course_id, self.grade]
