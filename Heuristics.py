"""Heuristics for the 8-puzzle.

These functions estimate how far a board is from the goal state:
- Heuristic1 counts misplaced tiles.
- Heuristic2 computes Manhattan distance for each tile.

The project currently uses a 3x3 board represented as a list of nine values,
with 0 as the empty tile. The goal state is treated as [1, 2, 3, 4, 5, 6, 7, 8, 0],
so the empty tile is ignored in the heuristic calculations.
"""

from Puzzle.PuzzleFunctions import checkInput
from Puzzle.Puzzle import Puzzle  # kept for local testing only


def Heuristic1(puzzle):
    """Return the number of tiles that are not in their goal positions."""
    checkInput(puzzle)
    hVal = 0
    for i in range(1, len(puzzle)):
        if i != puzzle[i]:
            hVal += 1
    return hVal


def Heuristic2(puzzle):
    """Return the sum of Manhattan distances for all non-zero tiles.

    For the standard 8-puzzle goal state [1, 2, 3, 4, 5, 6, 7, 8, 0], the
    blank tile is ignored because it does not contribute to the heuristic.
    """
    checkInput(puzzle)
    hVal = 0
    for i in range(0, len(puzzle)):
        value = puzzle[i]
        if value == 0:
            continue

        # Goal row/column for a tile in a 3x3 board.
        goal_row = (value - 1) // 3
        goal_col = (value - 1) % 3

        # Current row/column of the tile in the puzzle.
        current_row = i // 3
        current_col = i % 3

        # Manhattan distance: row difference + column difference.
        manhattan_distance = abs(goal_row - current_row) + abs(goal_col - current_col)
        hVal += manhattan_distance

    return hVal


# Tests kept for debugging and local validation.
# myPuzzle = Puzzle()
# for i in range(0, 1):
#     puz = myPuzzle.generate()
#     print(puz)
#     print(Heuristic2(puz))

# testPuz = [7, 2, 4, 5, 0, 6, 8, 3, 1]
# print(Heuristic2(testPuz))
