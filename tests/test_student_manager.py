"""
test_student_manager.py
------------------------
Basic unit tests using Python's built-in unittest module.
Run with:  python -m unittest discover tests
"""

import unittest
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import student_manager


class TestStudentManager(unittest.TestCase):

    def setUp(self):
        # Point the manager at a throwaway test file so real data is untouched.
        self.original_file = student_manager.DATA_FILE
        student_manager.DATA_FILE = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "test_students.csv"
        )
        if os.path.exists(student_manager.DATA_FILE):
            os.remove(student_manager.DATA_FILE)

    def tearDown(self):
        if os.path.exists(student_manager.DATA_FILE):
            os.remove(student_manager.DATA_FILE)
        student_manager.DATA_FILE = self.original_file

    def test_add_and_view_student(self):
        ok, msg = student_manager.add_student("S1", "Asha Rao", "asha@example.com", "CSE")
        self.assertTrue(ok)
        students = student_manager.view_students()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0]["name"], "Asha Rao")

    def test_duplicate_student_id_rejected(self):
        student_manager.add_student("S1", "Asha Rao", "asha@example.com", "CSE")
        ok, msg = student_manager.add_student("S1", "Someone Else", "x@example.com", "ECE")
        self.assertFalse(ok)

    def test_invalid_email_rejected(self):
        ok, msg = student_manager.add_student("S2", "Bad Email", "not-an-email", "CSE")
        self.assertFalse(ok)

    def test_update_student(self):
        student_manager.add_student("S3", "Old Name", "old@example.com", "CSE")
        ok, msg = student_manager.update_student("S3", name="New Name")
        self.assertTrue(ok)
        self.assertEqual(student_manager.find_student("S3")["name"], "New Name")

    def test_delete_student(self):
        student_manager.add_student("S4", "To Delete", "d@example.com", "CSE")
        ok, msg = student_manager.delete_student("S4")
        self.assertTrue(ok)
        self.assertIsNone(student_manager.find_student("S4"))


if __name__ == "__main__":
    unittest.main()
