import unittest
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import course_manager


class TestCourseManager(unittest.TestCase):

    def setUp(self):
        self.original_file = course_manager.DATA_FILE
        course_manager.DATA_FILE = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "test_courses.csv"
        )
        if os.path.exists(course_manager.DATA_FILE):
            os.remove(course_manager.DATA_FILE)

    def tearDown(self):
        if os.path.exists(course_manager.DATA_FILE):
            os.remove(course_manager.DATA_FILE)
        course_manager.DATA_FILE = self.original_file

    def test_add_and_view_course(self):
        ok, msg = course_manager.add_course("C1", "Python Essentials", "4", "Dr. Rao")
        self.assertTrue(ok)
        courses = course_manager.view_courses()
        self.assertEqual(len(courses), 1)

    def test_invalid_credits_rejected(self):
        ok, msg = course_manager.add_course("C2", "Bad Course", "abc", "Dr. Rao")
        self.assertFalse(ok)

    def test_delete_course(self):
        course_manager.add_course("C3", "Temp Course", "3", "Dr. Rao")
        ok, msg = course_manager.delete_course("C3")
        self.assertTrue(ok)
        self.assertIsNone(course_manager.find_course("C3"))


if __name__ == "__main__":
    unittest.main()
