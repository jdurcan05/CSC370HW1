from Puzzle.PuzzleFunctions import checkInput
from Puzzle.Puzzle import Puzzle

def Heuristic1(puzzle):
    checkInput(puzzle)
    hVal = 0
    for i in range(1, len(puzzle)):
        if i != puzzle[i]:
            hVal = hVal + 1
    return hVal





def Heuristic2():
    return None


myPuzzle = Puzzle()
for i in range (0,15):
    puz = myPuzzle.generate()
    print(puz)
    print(Heuristic1(puz))