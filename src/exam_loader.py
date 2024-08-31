from json import load as json_load
from os import path
from yaml import safe_load as yaml_load

EXAMS_DIR = '../exams'


def load_exam(exam_name):
    # Construct the file paths
    json_path = path.join(EXAMS_DIR, f"{exam_name}.json")
    yaml_path = path.join(EXAMS_DIR, f"{exam_name}.yaml")

    # Load JSON file if it exists
    if path.isfile(json_path):
        with open(json_path, 'r') as file:
            data = json_load(file)
        return data

    # Load YAML file if it exists
    if path.isfile(yaml_path):
        with open(yaml_path, 'r') as file:
            data = yaml_load(file)
        return data

    # Raise error if it does not exist
    raise FileNotFoundError(f"Exam file '{exam_name}' not found.")

    # Console log if exam name does not correspond to a json or yaml file
    # TODO: Add console logging
