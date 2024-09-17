def handle_multiple_choice(question) -> str:
    keys = [(i + 1) for i in range(len(question['options']))]
    question_dict = dict(zip(keys, question['options']))

    print(question['question'])
    for key, option in question_dict.items():
        print(f"{key}: {option}")

    answer = None
    question_answered = False

    while not question_answered:
        try:
            answer = input("Select an answer: ")
            answer = int(answer)
            if answer in question_dict:
                question_answered = True
            else:
                print("Invalid selection. Please enter a number corresponding to one of the options.")
        except ValueError:
            print("Invalid selection. Please enter a number corresponding to one of the options.")

    return question_dict[answer]


def handle_multiple_selection(question: dict) -> list:
    keys = [(i + 1) for i in range(len(question['options']))]
    question_dict = dict(zip(keys, question['options']))

    print(question['question'])
    for key, option in question_dict.items():
        print(f'{key}: {option}')

    answers = input('Select answer (comma-separated): ').replace(" ", "").split(',')
    mapped_answers = []
    for answer in answers:
        mapped_answers.append(question_dict[int(answer)])

    return mapped_answers


def handle_true_false(question: dict) -> str:
    print(question['question'])
    answer = input("True or False: ").strip().capitalize()
    return answer


def handle_fill_in_blank(question: dict) -> str:
    print(question['question'])
    answer = input("Your answer: ").strip()
    return answer


def calculate_results(answers: list) -> dict:
    num_answer_correct = 0

    for answer in answers:
        if answer.lower() == 'correct':
            num_answer_correct += 1

    results_percent = (num_answer_correct / len(answers)) * 100

    return {
        'total_num_answers': len(answers),
        'num_answer_correct': num_answer_correct,
        'results_percent': results_percent,
    }
