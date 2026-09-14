import random


class Puzzle:
    """Generates a 3x3 sliding puzzle board that is solvable"""
    def generate(self):
        """Generate a random 3x3 solvable board"""
        while 1:
            board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            random.shuffle(board)
            if self._is_solvable(board):
                return board

    @staticmethod
    def _is_solvable(board):
        """Checks if a generated board is solvable, returns true if solvable"""
        actual = board[:]
        target = [1, 2, 3, 4, 5, 6, 7, 8]

        actual.remove(0)

        cycles = 0
        frontier = []

        for i in range(8):
            if i not in frontier:
                cycle_val = i + 1
                cycles += Puzzle._is_solvable_helper(target, actual, i, cycle_val, frontier)

        return not (8 - cycles) % 2

    @staticmethod
    def _is_solvable_helper( board, actual, i, cycle_val, frontier):
        """Helper to trace each index"""
        if actual[i] == cycle_val:
            frontier.append(i)
            return 1

        val = actual[i]

        if i in frontier:
            return 0

        frontier.append(i)

        new_index = board.index(val)

        return Puzzle._is_solvable_helper(board, actual, new_index, cycle_val, frontier)

if __name__ == "__main__":
    test_board = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    print(Puzzle._is_solvable(test_board))