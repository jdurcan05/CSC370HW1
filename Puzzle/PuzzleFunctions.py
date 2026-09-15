"""Helpers for checking and expanding a 3x3 sliding-puzzle state.

A puzzle is represented by a list of nine values in row-major order. The
value ``0`` represents the empty position, and the completed state is
``[0, 1, 2, 3, 4, 5, 6, 7, 8]``.
"""

def checkInput(puzzle):
    """Exit with an error when ``puzzle`` does not contain nine positions."""
    if len(puzzle) != 9:
        print("Bad input: puzzle length off.")
        exit(1)
    


def isCompleted(puzzle):
    """Return whether ``puzzle`` is in the completed goal state."""
    checkInput(puzzle)
    for i in range(0, len(puzzle)):
        if(puzzle[i] != i):
            return False

    return True

def returnPermutations(puzzle):
    """Return states reachable by one legal move.

    Results are ordered up, right, left, down when those moves are valid.
    The input puzzle is not modified.
    """
    checkInput(puzzle)
    zeroLoc = 0
    permutations = []
    for i in range(0, len(puzzle)):
        if puzzle[i] == 0:
            zeroLoc = i
            break
    #Check all 4 ways that the 0 could go
    if zeroLoc >2:
        permutations.append(swapNums(puzzle, zeroLoc, zeroLoc-3))
    if zeroLoc%3 != 2:
        permutations.append(swapNums(puzzle, zeroLoc, zeroLoc+1))
    if zeroLoc%3 != 0:
        permutations.append(swapNums(puzzle, zeroLoc, zeroLoc-1))
    if zeroLoc < 6:
        permutations.append(swapNums(puzzle, zeroLoc, zeroLoc+3))
    return permutations


def swapNums(puzzle, spot1, spot2):
    """Return a copy of ``puzzle`` with two positions exchanged."""
    puzzleCopy = puzzle.copy()
    temp = puzzle[spot1]
    puzzleCopy[spot1] = puzzle[spot2]
    puzzleCopy[spot2] = temp
    return puzzleCopy
