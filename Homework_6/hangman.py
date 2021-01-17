from words import pick_a_word


def start():
    step = 0
    word = pick_a_word().upper()
    letters = set(word)
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
            if letter in tries:
                print(f' {letter} ', end='')
            else:
                print(f' _ ', end='')
        print()

        guess = input('Guess a letter: ').upper()
        if guess not in word:
            step += 1
        tries.add(guess)

    if step == 5:
        print('You lost the game.')


if __name__ == '__main__':
    start()
# print(__name__)

