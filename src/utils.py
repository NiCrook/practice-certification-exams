def handle_multiple_choice(question):
    print(question['question'])
    for key, option in question['options'].items():
        print(f"{key}: {option}")
    answer = input("Select an answer: ").strip()
    return answer


def handle_multiple_selection(question):
    print(question['question'])
    for key, option in question['options'].items():
        print(f"{key}: {option}")
    answers = input("Select answers (comma-separated): ").strip().split(',')
    return [ans.strip() for ans in answers]


def handle_true_false(question):
    print(question['question'])
    answer = input("True or False: ").strip().lower()
    return answer


def handle_fill_in_the_blank(question):
    print(question['question'])
    answer = input("Your answer: ").strip()
    return answer
