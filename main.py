from copy import deepcopy
from random import randint, choice

from move import Move
from cube import Cube
from config import *

MOVE_LETTERS = 'FBRLUD'
AXIS_MAP = {
    'F': 'Z', 'B': 'Z',
    'R': 'X', 'L': 'X',
    'U': 'Y', 'D': 'Y'
}

def randomize():
    letter = choice(MOVE_LETTERS)
    direction = 1 if randint(0, 100) < INVERTION_CHANCE else 0
    amount = 1 if randint(0, 100) < DOUBLE_CHANCE else 0

    return letter, direction, amount

scrambles = []
for _ in range(SCRAMBLES_AMOUNT):
    cube = Cube()
    state_history = []
    moves = []
    moves_amount = randint(*list(map(int, AMOUNT.split('-')))) if AMOUNT else randint(20, 25)
    while len(moves) < moves_amount:
        letter, direction, amount = randomize()
        
        if moves and letter == moves[-1].letter:
            continue

        if len(moves) > 1:
            axis_m1 = AXIS_MAP[moves[-2].letter]
            axis_m2 = AXIS_MAP[moves[-1].letter]
            axis_candidate = AXIS_MAP[letter]

            if axis_m1 == axis_m2 == axis_candidate:
                continue
        
        cube.move(letter, direction, amount)
        current_state = deepcopy(cube.state)

        if current_state in state_history:
            continue
        
        state_history.append(current_state)
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
