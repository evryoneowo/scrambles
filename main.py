from random import randint, choice

from move import Move

MOVE_LETTERS = 'FBRLUD'
AXIS_MAP = {
    'F': 'Z', 'B': 'Z',
    'R': 'X', 'L': 'X',
    'U': 'Y', 'D': 'Y'
}

MOVES_AMOUNT = randint(20, 25)

def randomize():
    letter = choice(MOVE_LETTERS)
    direction = 0 if randint(0, 2) else 1
    amount = 0 if randint(0, 3) else 1

    return letter, direction, amount

print(f'{MOVES_AMOUNT} moves in total')

moves = [Move(*randomize())]
for i in range(MOVES_AMOUNT-1):
    letter, direction, amount = randomize()
    
    while letter == moves[-1].letter:
        letter, direction, amount = randomize()

    if i:
        axis_m1 = AXIS_MAP[moves[-2].letter]
        axis_m2 = AXIS_MAP[moves[-1].letter]
        axis_m3 = AXIS_MAP[letter]

        while (axis_m1 == axis_m2 and axis_m2 == axis_m3) or letter == moves[-1].letter:
            letter, direction, amount = randomize()
            axis_m3 = AXIS_MAP[letter]

    moves.append(Move(letter, direction, amount))

print(' '.join(map(str, moves)))
input()