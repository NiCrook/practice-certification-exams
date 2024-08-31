from os import listdir, path
from unittest import TestCase
from unittest import main as unittest_main

from src.exam_loader import load_exam


class TestExamLoader(TestCase):

    def test_load_exam__all_exams(self):
        # Directory containing exam files
        exams_dir = '../exams'

        # List all files in the exams directory
        for file_name in listdir(exams_dir):
            if file_name.endswith('.json') or file_name.endswith('.yaml'):
                # Extract exam name (without extension)
                exam_name, _ = path.splitext(file_name)

                try:
                    # Attempt to load the exam file
                    exam_data = load_exam(exam_name)
                    self.assertIsNotNone(exam_data, f"Failed to load exam data for '{exam_name}'")
                except Exception as e:
                    self.fail(f"Loading exam file '{file_name}' failed with exception: {e}")


if __name__ == '__main__':
    unittest_main()
