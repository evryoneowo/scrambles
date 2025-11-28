class Move:
    def __init__(self, letter: str, direction: int, amount: int):
        self.letter = letter
        self.direction = direction
        self.amount = amount

    def __str__(self) -> str:
        if self.amount:
            return f'{self.letter}2'
        else:
            return self.letter + ('\'' if self.direction else '')