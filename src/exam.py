from datetime import datetime, timedelta
from exam_loader import get_exam_names, load_exam
from random import choice as random_choice
from src.utils import (
    calculate_results,
    handle_multiple_choice,
    handle_multiple_selection,
    handle_true_false,
    handle_fill_in_blank
)


class Exam:
    def __init__(self, exam_name_):
        self.exam_name = exam_name_
        self.exam_dir = '../exams'
        self.exam = load_exam(exam_name_, self.exam_dir)
        self.questions = self.exam.get('questions', [])
        self.time_duration = self.exam.get('time_duration')
        self.question_duration = self.exam.get('question_duration')
        self.used_questions = set()
        self.answers = []
        self.calculated_results = {}
        self.handlers = {
            'multiple_choice': handle_multiple_choice,
            'multiple_select': handle_multiple_selection,
            'true_false': handle_true_false,
            'fill_in_blank': handle_fill_in_blank
        }

    def get_random_question(self):
        available_questions = [q for i, q in enumerate(self.questions) if i not in self.used_questions]

        if not available_questions:
            return None

        question = random_choice(available_questions)
        self.used_questions.add(self.questions.index(question))
        return question

    def start(self):
        print(f"Starting the {self.exam_name} quiz...\n")

        start_time = datetime.now()
        print(f'start time: {start_time}')
        end_time = start_time + timedelta(seconds=self.time_duration)
        print(f'end time: {end_time}')

        question_count = 0
        while question_count < self.question_duration:
            current_time = datetime.now()
            if current_time > end_time:
                print("Time is up!")
                break

            question = self.get_random_question()
            if not question:
                print("No more questions left.")
                break

            self.ask_question(question)
            question_count += 1

        self.check_unanswered_questions()
        self.calculated_results = calculate_results(self.answers)

        print(
            f"\nResults- Time taken: {datetime.now() - start_time}"
            f"\nNumber of questions answered: {self.calculated_results['total_num_answers']}"
            f"\nNumber of questions answered correctly: {self.calculated_results['num_answer_correct']}"
            f"\nGrade: {self.calculated_results['results_percent']:.0f}%"
        )

    def ask_question(self, question):
        q_type = question['type']
        if q_type not in self.handlers:
            raise ValueError(f"Unknown question type: {q_type}")

        handler = self.handlers[q_type]
        user_answer = handler(question)
        self.check_answer(question['answer'], user_answer)

    def check_answer(self, correct_answer, user_answer):
        if isinstance(correct_answer, list):
            correct_answer = set(correct_answer)
            user_answer = set(user_answer)
            if user_answer == correct_answer:
                print("Correct!")
                self.answers.append('Correct')
            else:
                print(f"Incorrect!\nThe correct answer(s): \n{',\n'.join(correct_answer)}")
                self.answers.append('Incorrect')
        else:
            if user_answer == correct_answer:
                print("Correct!")
                self.answers.append('Correct')
            else:
                print(f"Incorrect!\nThe correct answer:\n{correct_answer}")
                self.answers.append('Incorrect')

        print()

    def check_unanswered_questions(self):
        unanswered_questions = len(self.questions) - len(self.used_questions)
        if unanswered_questions > 0:
            print(f"{unanswered_questions} questions were not answered due to time constraints.")
            # TODO: Mark unanswered questions as incorrect


if __name__ == '__main__':
    exam_dir = '../exams'
    print("Review available exams:")
    print(get_exam_names(exam_dir))
    exam_name = input("Enter the exam name: ").strip()
    quiz = Exam(exam_name)
    quiz.start()
