from random import randint, choice

from move import Move
from config import *

MOVE_LETTERS = 'FBRLUD'
AXIS_MAP = {
    'F': 'Z', 'B': 'Z',
    'R': 'X', 'L': 'X',
    'U': 'Y', 'D': 'Y'
}

MOVES_AMOUNT = AMOUNT if AMOUNT else randint(20, 25)

def randomize():
    letter = choice(MOVE_LETTERS)
    direction = 0 if randint(0, 100) < INVERTION_CHANCE else 1
    amount = 0 if randint(0, 100) < DOUBLE_CHANCE else 1

    return letter, direction, amount

scrambles = []
for _ in range(SCRAMBLES_AMOUNT):
    moves = []
    for i in range(MOVES_AMOUNT):
        letter, direction, amount = randomize()
        
        if moves and letter == moves[-1].letter:
            continue

        if len(moves) > 1:
            axis_m1 = AXIS_MAP[moves[-2].letter]
            axis_m2 = AXIS_MAP[moves[-1].letter]
            axis_candidate = AXIS_MAP[letter]

            if axis_m1 == axis_m2 == axis_candidate:
                continue

        moves.append(Move(letter, direction, amount))
    
    scrambles.append(moves)

txts = [f'{len(scramble)} moves in total\n{' '.join(map(str, scramble))}\n' for scramble in scrambles]

if SAVE_TO_FILE:
    with open(SAVE_TO_FILE, 'w') as f:
        f.write('\n'.join(txts))
else:
    for txt in txts:
        print(txt)
    input()
