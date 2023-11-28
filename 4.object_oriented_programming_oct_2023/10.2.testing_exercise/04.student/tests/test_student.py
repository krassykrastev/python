from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student1 = Student("Student1", {"Python": ["note1", "note2", "note3"], "JS": ["note1", "note2"]})
        self.student2 = Student("Student2")

    def test_init_with_courses(self):
        self.assertEqual(self.student1.name, "Student1")
        self.assertEqual(self.student1.courses, {"Python": ["note1", "note2", "note3"], "JS": ["note1", "note2"]})

    def test_init_without_courses(self):
        self.assertEqual(self.student2.name, "Student2")
        self.assertEqual(self.student2.courses, {})

    def test_enroll_existing_course(self):
        result = self.student1.enroll("Python", ["note4", "note5"], "Y")
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(self.student1.courses, {"Python": ["note1", "note2", "note3", "note4", "note5"], "JS": ["note1", "note2"]})

    def test_enroll_non_existing_course_y(self):
        result = self.student1.enroll("C#", ["note1", "note2"], "Y")
        self.assertIn("C#", self.student1.courses)
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["note1", "note2"], self.student1.courses["C#"])

    def test_enroll_non_existing_course_with_empty_string(self):
        result = self.student1.enroll("C#", ["note1", "note2"], "")
        self.assertIn("C#", self.student1.courses)
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["note1", "note2"], self.student1.courses["C#"])

    def test_enroll_non_existing_course_not_having_notes(self):
        result = self.student1.enroll("C#", ["note1", "note2"], "N")
        self.assertIn("C#", self.student1.courses)
        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.student1.courses["C#"])

    def test_add_notes_to_existing_course(self):
        self.student2.enroll("C#", ["note1", "note2"], "Y")
        result = self.student2.add_notes("C#", "note3")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(self.student2.courses, {"C#": ["note1", "note2", "note3"]})

    def test_add_notes_to_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student2.add_notes("C#", "note3")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_existing_course(self):
        result = self.student1.leave_course("Python")
        self.assertEqual("Course has been removed", result)
        self.assertNotIn("Python", self.student1.courses)

    def test_leave_course_not_found(self):
        with self.assertRaises(Exception) as ex:
            self.student1.leave_course("C#")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
