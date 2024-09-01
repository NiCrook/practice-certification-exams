def handle_multiple_choice(question) -> str:
    keys = [(i + 1) for i in range(len(question['options']))]
    question_dict = dict(zip(keys, question['options']))

    print(question['question'])
    for key, option in question_dict.items():
        print(f"{key}: {option}")

    answer = input("Select an answer: ")
    answer = question_dict[int(answer)]

    return answer


def handle_multiple_selection(question: dict) -> list:
    keys = [(i + 1) for i in range(len(question['options']))]
    question_dict = dict(zip(keys, question['options']))

    print(question['question'])
    for key, option in question_dict.items():
        print(f'{key}: {option}')

    answers = input("Select answers (comma-separated): ").strip().split(', ')
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
