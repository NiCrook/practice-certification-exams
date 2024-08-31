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
            'options': {
                'a': 'Paris',
                'b': 'London',
                'c': 'Rome'
            },
            'answer': 'a'
        }

        inputs = ['a']
        with patch('builtins.input', side_effect=mock_input(inputs)):
            answer = handle_multiple_choice(question)
            self.assertEqual(answer, 'a')

    def test_handle_multiple_selection(self):
        question = {
            'question': 'Select all the programming languages:',
            'type': 'multiple_selection',
            'options': {
                'a': 'Python',
                'b': 'Java',
                'c': 'HTML'
            },
            'answers': ['a', 'b']
        }

        inputs = ['a, b']
        with patch('builtins.input', side_effect=mock_input(inputs)):
            answers = handle_multiple_selection(question)
            self.assertEqual(answers, ['a', 'b'])

    def test_handle_true_false(self):
        question = {
            'question': 'Is Python a programming language?',
            'type': 'true_false',
            'answer': 'true'
        }

        inputs = ['true']
        with patch('builtins.input', side_effect=mock_input(inputs)):
            answer = handle_true_false(question)
            self.assertEqual(answer, 'true')

    def test_handle_fill_in_the_blank(self):
        question = {
            'question': 'Infrastructure as ____.',
            'type': 'fill_in_the_blank',
            'answer': 'Code'
        }

        inputs = ['Code']
        with patch('builtins.input', side_effect=mock_input(inputs)):
            answer = handle_fill_in_the_blank(question)
            self.assertEqual(answer, 'Code')


if __name__ == '__main__':
    unittest_main()
