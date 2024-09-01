from unittest import main as unittest_main
from unittest import TestCase
from unittest.mock import patch

from src.utils import (
    handle_multiple_choice,
    handle_multiple_selection,
    handle_true_false,
    handle_fill_in_the_blank
)


def mock_input(inputs):
    """Helper function to mock user input."""

    def _mock_input(prompt):
        return inputs.pop(0)

    return _mock_input


class TestQuestionHandlers(TestCase):
    def test_handle_multiple_choice(self):
        question = {
            'question': 'What is the capital of France?',
            'type': 'multiple_choice',
            'options': ['Paris', 'London', 'Rome'],
            'answer': 'Paris'
        }

        user_input = 1
        with patch('builtins.input', return_value=user_input):
            answer = handle_multiple_choice(question)
            self.assertEqual(answer, 'Paris')

    def test_handle_multiple_selection(self):
        question = {
            'question': 'Select all the programming languages:',
            'type': 'multiple_selection',
            'options': ['Python', 'Java', 'English'],
            'answers': ['Python', 'Java']
        }

        user_input = ["1, 2"]
        with patch('builtins.input', side_effect=mock_input(user_input)):
            answers = handle_multiple_selection(question)
            self.assertEqual(answers, ['Python', 'Java'])

    def test_handle_true_false(self):
        question = {
            'question': 'Is Python a programming language?',
            'type': 'true_false',
            'answer': 'true'
        }

        user_input = ['true']
        with patch('builtins.input', side_effect=mock_input(user_input)):
            answer = handle_true_false(question)
            self.assertEqual(answer, 'True')

    def test_handle_fill_in_the_blank(self):
        question = {
            'question': 'Infrastructure as ____.',
            'type': 'fill_in_the_blank',
            'answer': 'Code'
        }

        user_input = ['Code']
        with patch('builtins.input', side_effect=mock_input(user_input)):
            answer = handle_fill_in_the_blank(question)
            self.assertEqual(answer, 'Code')


if __name__ == '__main__':
    unittest_main()
