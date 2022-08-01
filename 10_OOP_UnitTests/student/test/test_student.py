import unittest

from project.student import Student


class TestStudent(unittest.TestCase):
    def test_student_obj_initializes_without_courses(self):
        s = Student('Test')
        self.assertEqual('Test', s.name)
        self.assertEqual({}, s.courses)

    def test_student_obj_initializes_with_courses(self):
        s = Student('Test', {'Python': []})
        self.assertEqual('Test', s.name)
        self.assertEqual({'Python': []}, s.courses)

    def test_enroll_method_updates_notes_when_course_added(self):
        s = Student('Test', {'Python': []})
        result = s.enroll('Python', ['testnote'], '')
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(['testnote'], s.courses['Python'])

    def test_enroll_method_updates_when_y_in_add_course_notes(self):
        s = Student('Test', {})
        result = s.enroll('Python', ['testnote1', 'testnote2'], 'Y')
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(s.courses['Python'], ['testnote1', 'testnote2'])

    def test_enroll_method_updates_when_empty_string_in_add_course_notes(self):
        s = Student('Test', {})
        result = s.enroll('Python', ['testnote1', 'testnote2'], '')
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(s.courses['Python'], ['testnote1', 'testnote2'])

    def test_enroll_method_updates_when_course_not_in_courses_and_notes_different(self):
        s = Student('Test', {})
        result = s.enroll('Python', ['testnote'], 'tt')
        self.assertEqual("Course has been added.", result)
        self.assertEqual(s.courses['Python'], [])

    def test_add_notes_method_raises_when_course_not_available(self):
        s = Student('Test', {})
        with self.assertRaises(Exception) as err:
            s.add_notes('Python', ['test'])
        self.assertEqual("Cannot add notes. Course not found.", str(err.exception))

    def test_add_notes_method_updates_notes_correct(self):
        s = Student('Test', {'Python': ['testnote1', 'test']})
        result = s.add_notes('Python', 'testnote3')
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(s.courses['Python'], ['testnote1', 'test', 'testnote3'])

    def test_leave_course_method_raises_when_course_not_found(self):
        s = Student('Test', {'Python': ['testnote']})
        with self.assertRaises(Exception) as err:
            s.leave_course('Java')
        self.assertEqual("Cannot remove course. Course not found.", str(err.exception))

    def test_leave_course_method_works_correct_when_course_is_available(self):
        s = Student('Test', {'Python': ['testnote']})
        result = s.leave_course('Python')
        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, s.courses)


if __name__ == '__main__':
    unittest.main()
