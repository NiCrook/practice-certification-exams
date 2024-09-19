from json import load as json_load
from os import listdir, path
from unittest import TestCase
from unittest import main as unittest_main
from unittest.mock import patch

from src.exam_loader import get_exam_names, load_exam


def load_exam_files(directory_path):
    exam_files = []
    for filename in listdir(directory_path):
        if filename.endswith('.json'):
            with open(path.join(directory_path, filename), 'r') as file:
                exam_files.append(json_load(file))

    return exam_files


class TestExamLoader(TestCase):

    def setUp(self) -> None:
        self.exam_files = load_exam_files('../exams')

    def test_time_duration(self):
        for exam in self.exam_files:
            with self.subTest(exam=exam):
                self.assertIn('time_duration', exam)
                self.assertIsInstance(exam['time_duration'], int)

    def test_question_duration(self):
        for exam in self.exam_files:
            with self.subTest(exam=exam):
                self.assertIn('question_duration', exam)
                self.assertIsInstance(exam['question_duration'], int)

    def test_questions_structure(self):
        for exam in self.exam_files:
            with self.subTest(exam=exam):
                self.assertIn('questions', exam)
                self.assertIsInstance(exam['questions'], list)

                for question in exam['questions']:
                    self.assertIn('question', question)
                    self.assertIn('answer', question)
                    self.assertIn('type', question)
                    self.assertIsInstance('question', str)
                    self.assertIsInstance('type', str)

                    question_type = question['type']

                    if question_type == 'multiple_choice':
                        print(f'Question: {question}')
                        self.assertIsInstance(question['answer'], str)
                        self.assertIsInstance(question['options'], list)
                        self.assertGreater(len(question['options']), 0)
                        for option in question['options']:
                            self.assertIsInstance(option, str)

                    if question_type == 'multiple_select':
                        print(f'Question: {question}')
                        print(type(question['answer']))
                        self.assertIsInstance(question['answer'], list)
                        self.assertIn('options', question)
                        self.assertIsInstance(question['options'], list)
                        self.assertGreater(len(question['options']), 0)

                    elif question_type == 'true_false':
                        print(f'Question: {question}')
                        self.assertIn(question['answer'], ['True', 'False'])

    @patch('src.exam_loader.load_exam')
    def test_load_exam__all_exams(self, test_exam_directory_path):
        test_exam_directory_path.return_value = ['one.json', 'two.json']

        for file_name in test_exam_directory_path:
            if file_name.endswith('.json') or file_name.endswith('.yaml'):
                exam_name, _ = path.splitext(file_name)

                try:
                    exam_data = load_exam(exam_name, test_exam_directory_path)
                    self.assertIsNotNone(exam_data, f"Failed to load exam data for '{exam_name}'")
                except Exception as e:
                    self.fail(f"Loading exam file '{file_name}' failed with exception: {e}")

    @patch('os.listdir')
    def test_get_exam_names(self, test_exam_dir):
        test_exam_dir.return_value = ['one.json', 'two.json']

        result = get_exam_names('test/path')

        assert result == ['one', 'two']


if __name__ == '__main__':
    unittest_main()
