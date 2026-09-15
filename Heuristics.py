"""Heuristics for the 8-puzzle.

These functions estimate how far a board is from the goal state:
- Heuristic1 counts misplaced tiles.
- Heuristic2 computes Manhattan distance for each tile.
- Heuristic3 computes moves used in a relaxed adjacency model

The project currently uses a 3x3 board represented as a list of nine values,
with 0 as the empty tile. The goal state is treated as [0,1,2,3,4,5,6,7,8]
"""

from Puzzle.PuzzleFunctions import checkInput, isCompleted
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
    """Return the sum of Manhattan distances for all non-zero tiles."""
    checkInput(puzzle)
    hVal = 0
    for i in range(0, len(puzzle)):
        value = puzzle[i]
        if (value == 0):
            continue

        # Goal row/column for a tile in a 3x3 board.
        goal_row = (value) // 3
        goal_col = (value) % 3

        # Current row/column of the tile in the puzzle.
        current_row = i // 3
        current_col = i % 3

        # Manhattan distance: row difference + column difference.
        manhattan_distance = abs(goal_row - current_row) + abs(goal_col - current_col)
        hVal += manhattan_distance

    return hVal

#Relaxed adjacency heuristic (Cucs 1985)
def Heuristic3(puzzleInput):
    """Return the amount of moves without adjacency constraint."""
    checkInput(puzzleInput)
    puzzle = puzzleInput.copy()
    moves = 0

    while(not isCompleted(puzzle)):
        if (puzzle[0] == 0):
            for i in range(1, len(puzzle)):
                if(puzzle[i] != i):
                    puzzle[0] = puzzle[i]
                    puzzle[i] = 0
                    break
        else:
            zero_position = 0
            for i in range(1, len(puzzle)):
                if(puzzle[i] == 0):
                    zero_position = i
                    break
            for i in range(len(puzzle)):
                if(puzzle[i] == zero_position):
                    puzzle[zero_position] = puzzle[i]
                    puzzle[i] = 0
                    break

        moves = moves+1
    return moves
