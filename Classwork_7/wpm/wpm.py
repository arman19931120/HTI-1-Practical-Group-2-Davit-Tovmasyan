import time
# import sys

import zen
# from armenian import hy


def collect_data(sentence):
    print(sentence)
    start = time.time()
    typed = input()
    duration = time.time() - start
    return typed, duration


def formula(original_text, typed_text, duration):

    errors = len(original_text)

    for i, j in zip(original_text, typed_text):
        if i == j:
            errors -= 1

    score = 60 * (len(original_text) / 5 - errors / duration) / duration
    accuracy = 100 - errors * 100 // len(original_text)

    return {
        'score': score,
        'accuracy': accuracy,
    }


def main():
    # if len(sys.argv) > 1 and sys.argv[1] == 'arm':
    #     sentence = hy.get_a_sentence()
    # else:
    #     sentence = zen.get_a_sentence()

    sentence = zen.zen.get_a_sentence()

    typed, duration = collect_data(sentence)
    result = formula(sentence, typed, duration)
    print('Your score is {score}. Accuracy is {accuracy}%.'.format(**result))


if __name__ == '__main__':
    main()
