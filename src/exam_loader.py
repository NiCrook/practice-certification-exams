import os
from json import load as json_load
from os import path
from yaml import safe_load as yaml_load


def get_exam_names(exam_directory: str) -> list:
    exam_paths = []

    for exam in os.listdir(exam_directory):
        if '.json' in exam:
            exam_paths.append(exam.replace('.json', ''))

    return exam_paths


def load_exam(exam_name: str, exam_directory: str) -> any:
    json_path = path.join(exam_directory, f"{exam_name}.json")
    yaml_path = path.join(exam_directory, f"{exam_name}.yaml")

    if path.isfile(json_path):
        with open(json_path, 'r') as file:
            data = json_load(file)
        return data

    if path.isfile(yaml_path):
        with open(yaml_path, 'r') as file:
            data = yaml_load(file)
        return data

    raise FileNotFoundError(f"Exam file '{exam_name}' not found.")

    # Console log if exam name does not correspond to a json or yaml file
    # TODO: Add console logging
