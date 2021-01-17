import os
import random


def pick_a_word():
    file_path = os.path.abspath(__file__)
    current_dir = os.path.dirname(file_path)
    with open(os.path.join(current_dir, 'words.txt')) as f:
        return random.choice(f.readlines()).rstrip()
