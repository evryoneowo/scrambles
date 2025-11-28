COLORS = {
    'W': 'White',
    'Y': 'Yellow',
    'R': 'Red',
    'O': 'Orange',
    'B': 'Blue',
    'G': 'Green'
}

OPPOSITES = {
    'F': 'B',
    'B': 'F',
    'R': 'L',
    'L': 'R',
    'U': 'D',
    'D': 'U'
}

class Cube:
    def __init__(self):
        self.state = {
            'F': ['G'] * 9,
            'B': ['B'] * 9,
            'R': ['R'] * 9,
            'L': ['O'] * 9,
            'U': ['W'] * 9,
            'D': ['Y'] * 9
        }
    
    def move(self, face, inverted, double):
        cycles = {
            'F': [
                [('U', 6), ('R', 0), ('D', 2), ('L', 8)],
                [('U', 7), ('R', 3), ('D', 1), ('L', 5)],
                [('U', 8), ('R', 6), ('D', 0), ('L', 2)],
            ],
            'B': [
                [('U', 0), ('L', 2), ('D', 8), ('R', 6)],
                [('U', 1), ('L', 5), ('D', 7), ('R', 3)],
                [('U', 2), ('L', 8), ('D', 6), ('R', 0)],
            ],
            'U': [
                [('B', 2), ('R', 2), ('F', 2), ('L', 2)],
                [('B', 1), ('R', 1), ('F', 1), ('L', 1)],
                [('B', 0), ('R', 0), ('F', 0), ('L', 0)],
            ],
            'D': [
                [('F', 6), ('R', 6), ('B', 6), ('L', 6)],
                [('F', 7), ('R', 7), ('B', 7), ('L', 7)],
                [('F', 8), ('R', 8), ('B', 8), ('L', 8)],
            ],
            'R': [
                [('U', 8), ('B', 0), ('D', 2), ('F', 8)],
                [('U', 5), ('B', 3), ('D', 5), ('F', 5)],
                [('U', 2), ('B', 6), ('D', 8), ('F', 2)],
            ],
            'L': [
                [('U', 0), ('F', 0), ('D', 0), ('B', 8)],
                [('U', 3), ('F', 3), ('D', 3), ('B', 5)],
                [('U', 6), ('F', 6), ('D', 6), ('B', 2)],
            ]
        }
        
        turn_count = 2 if double else (3 if inverted else 1)

        for _ in range(turn_count):
            face_state = self.state[face]
            rotated_face = [face_state[i] for i in [6, 3, 0, 7, 4, 1, 8, 5, 2]]
            self.state[face] = rotated_face

            sticker_cycles = cycles[face]
            for cycle in sticker_cycles:
                
                cache = self.state[cycle[-1][0]][cycle[-1][1]]
                for i in range(len(cycle) - 1, 0, -1):
                    face_from, sticker_from = cycle[i-1]
                    face_to, sticker_to = cycle[i]
                    self.state[face_to][sticker_to] = self.state[face_from][sticker_from]
                
                self.state[cycle[0][0]][cycle[0][1]] = cache

cube = Cube()
print(cube.state)
cube.move('F', 0, 0)
cube.move('F', 1, 0)
print(cube.state)