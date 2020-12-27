import os
import random


def get_a_sentence():
    file_path = os.path.abspath(__file__)
    current_dir = os.path.dirname(file_path)
    with open(os.path.join(current_dir, 'zen.txt')) as f:
        return random.choice(f.readlines()).rstrip()
