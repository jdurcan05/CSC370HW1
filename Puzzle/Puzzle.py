import random

class Puzzle:
    def generate(self):
        while 1:
            board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            random.shuffle(board)
            if self._is_solvable(board):
                return board

    @staticmethod
    def _is_solvable(board):
        return 1
