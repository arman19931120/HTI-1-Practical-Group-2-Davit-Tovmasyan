def pick_a_word():
    return 'apple'


def start():
    step = 0
    word = pick_a_word()
    letters = set(word.upper())
    tries = set()
    while step < 5:
        if tries.issuperset(letters):
            for letter in word:
                print(f' {letter} ', end='')
            print()
            print('You won the game.')
            break
        print(f'Guess the word. {5 - step} mistakes left.')
        for letter in word:
            if letter.upper() in tries:
                print(f' {letter.upper()} ', end='')
            else:
                print(' _ ', end='')
        print()
        letter = input('Guess a letter: ').upper()
        if letter not in letters:
            step += 1
        tries.add(letter)


if __name__ == '__main__':
    start()
