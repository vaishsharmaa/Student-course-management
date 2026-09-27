"""
main.py
-------
Command-line entry point. Run with:  python main.py
This file only handles the menu/input loop — all real logic lives
in the app/ package, kept separate on purpose (see README).
"""

from app import student_manager, course_manager, enrollment_manager, reports


MENU = """
=========================================
 STUDENT & COURSE MANAGEMENT SYSTEM
=========================================
 1. Add student
 2. View all students
 3. Update student
 4. Delete student
 5. Add course
 6. View all courses
 7. Update course
 8. Delete course
 9. Enroll student in course
10. Set grade for an enrollment
11. Drop an enrollment
12. View all enrollments
13. Student transcript
14. Course roster
15. Enrollment summary
 0. Exit
=========================================
"""


def print_table(rows):
    if not rows:
        print("(no records found)")
        return
    headers = list(rows[0].keys())
    print(" | ".join(headers))
    print("-" * (len(headers) * 15))
    for row in rows:
        print(" | ".join(str(row[h]) for h in headers))


def main():
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            sid = input("Student ID: ").strip()
            name = input("Name: ").strip()
            email = input("Email: ").strip()
            dept = input("Department: ").strip()
            ok, msg = student_manager.add_student(sid, name, email, dept)
            print(msg)

        elif choice == "2":
            print_table(student_manager.view_students())

        elif choice == "3":
            sid = input("Student ID to update: ").strip()
            name = input("New name (blank to skip): ").strip()
            email = input("New email (blank to skip): ").strip()
            dept = input("New department (blank to skip): ").strip()
            ok, msg = student_manager.update_student(sid, name=name, email=email, department=dept)
            print(msg)

        elif choice == "4":
            sid = input("Student ID to delete: ").strip()
            ok, msg = student_manager.delete_student(sid)
            print(msg)

        elif choice == "5":
            cid = input("Course ID: ").strip()
            cname = input("Course name: ").strip()
            credits = input("Credits: ").strip()
            instructor = input("Instructor: ").strip()
            ok, msg = course_manager.add_course(cid, cname, credits, instructor)
            print(msg)

        elif choice == "6":
            print_table(course_manager.view_courses())

        elif choice == "7":
            cid = input("Course ID to update: ").strip()
            cname = input("New name (blank to skip): ").strip()
            credits = input("New credits (blank to skip): ").strip()
            instructor = input("New instructor (blank to skip): ").strip()
            ok, msg = course_manager.update_course(cid, course_name=cname, credits=credits, instructor=instructor)
            print(msg)

        elif choice == "8":
            cid = input("Course ID to delete: ").strip()
            ok, msg = course_manager.delete_course(cid)
            print(msg)

        elif choice == "9":
            sid = input("Student ID: ").strip()
            cid = input("Course ID: ").strip()
            ok, msg = enrollment_manager.enroll_student(sid, cid)
            print(msg)

        elif choice == "10":
            eid = input("Enrollment ID: ").strip()
            grade = input("Grade (e.g. A, B+): ").strip()
            ok, msg = enrollment_manager.set_grade(eid, grade)
            print(msg)

        elif choice == "11":
            eid = input("Enrollment ID to drop: ").strip()
            ok, msg = enrollment_manager.drop_enrollment(eid)
            print(msg)

        elif choice == "12":
            print_table(enrollment_manager.view_enrollments())

        elif choice == "13":
            sid = input("Student ID: ").strip()
            result = reports.student_transcript(sid)
            if result is None:
                print("Student not found.")
            else:
                print(f"\nTranscript for {result['student']['name']} ({sid}):")
                print_table(result["courses"])

        elif choice == "14":
            cid = input("Course ID: ").strip()
            result = reports.course_roster(cid)
            if result is None:
                print("Course not found.")
            else:
                print(f"\nRoster for {result['course']['course_name']} ({cid}):")
                print_table(result["students"])

        elif choice == "15":
            summary = reports.enrollment_summary()
            print(f"\nTotal students:    {summary['total_students']}")
            print(f"Total courses:     {summary['total_courses']}")
            print(f"Total enrollments: {summary['total_enrollments']}")
            if summary["most_popular_course"]:
                mp = summary["most_popular_course"]
                print(f"Most popular course: {mp['course_name']} ({mp['enrollment_count']} students)")
            else:
                print("Most popular course: N/A (no enrollments yet)")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
