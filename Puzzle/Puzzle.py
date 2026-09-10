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
        serpent = board
        serpent[3:5] = serpent[3:5][::-1]

        cycles = 0

        for i in range(8):
            cycles += Puzzle._is_solvable_helper(board, serpent, i)

        return not (8 - cycles % 2)

    @staticmethod
    def _is_solvable_helper(board, serpent, i):
        if serpent[i] == board[i]:
            return 1

        val = serpent[i]
        new_index = board.index(val)
        Puzzle._is_solvable_helper(board, serpent, new_index)
        return 0