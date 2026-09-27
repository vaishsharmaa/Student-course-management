"""
reports.py
----------
Read-only analytics built on top of the three managers.
Deliberately kept separate from enrollment_manager.py: this module
only *reads* data and formats it, it never writes, which keeps the
"write" and "report" responsibilities from tangling together.
"""

from app import student_manager, course_manager, enrollment_manager


def student_transcript(student_id):
    """All courses a given student is enrolled in, with grades."""
    student = student_manager.find_student(student_id)
    if not student:
        return None

    enrollments = [e for e in enrollment_manager.view_enrollments() if e["student_id"] == student_id]
    rows = []
    for e in enrollments:
        course = course_manager.find_course(e["course_id"])
        rows.append({
            "course_id": e["course_id"],
            "course_name": course["course_name"] if course else "Unknown",
            "grade": e["grade"] or "Not graded",
        })
    return {"student": student, "courses": rows}


def course_roster(course_id):
    """Every student enrolled in a given course."""
    course = course_manager.find_course(course_id)
    if not course:
        return None

    enrollments = [e for e in enrollment_manager.view_enrollments() if e["course_id"] == course_id]
    rows = []
    for e in enrollments:
        student = student_manager.find_student(e["student_id"])
        rows.append({
            "student_id": e["student_id"],
            "name": student["name"] if student else "Unknown",
            "grade": e["grade"] or "Not graded",
        })
    return {"course": course, "students": rows}


def enrollment_summary():
    """High-level counts: total students, courses, enrollments, and
    the most popular course by enrollment count."""
    students = student_manager.view_students()
    courses = course_manager.view_courses()
    enrollments = enrollment_manager.view_enrollments()

    counts = {}
    for e in enrollments:
        counts[e["course_id"]] = counts.get(e["course_id"], 0) + 1

    most_popular = None
    if counts:
        top_id = max(counts, key=counts.get)
        course = course_manager.find_course(top_id)
        most_popular = {
            "course_id": top_id,
            "course_name": course["course_name"] if course else "Unknown",
            "enrollment_count": counts[top_id],
        }

    return {
        "total_students": len(students),
        "total_courses": len(courses),
        "total_enrollments": len(enrollments),
        "most_popular_course": most_popular,
    }
