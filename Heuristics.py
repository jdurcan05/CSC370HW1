from Puzzle.PuzzleFunctions import checkInput
from Puzzle.Puzzle import Puzzle

def Heuristic1(puzzle):
    checkInput(puzzle)
    hVal = 0
    for i in range(1, len(puzzle)):
        if i != puzzle[i]:
            hVal = hVal + 1
    return hVal





def Heuristic2(puzzle):
    checkInput(puzzle)
    hVal = 0
    for i in range(0, len(puzzle)):
        #Check what is at this position (no need to check 0s)
        value = puzzle[i]
        if value == 0:
            continue

        #Find the values needed
        manDist = 0

        #Vertical distance (between 0 and 2)
        currentVertPosition = i%3
        idealVertPosition = value%3
        vertDistance = abs(currentVertPosition-idealVertPosition)

        #Horizontal distance (between 0 and 2)
        rowVal = int(value/3)
        rowi = int(i/3)
        horizDistance = int(abs(rowi-rowVal))

        #Aggregate
        manDist = vertDistance + horizDistance
        hVal = hVal + manDist

    return hVal

#Tests (TO be deleted)
# myPuzzle = Puzzle()
# for i in range (0,1):
#     puz = myPuzzle.generate()
#     print(puz)
#     print(Heuristic2(puz))

# testPuz = [7,2,4,5,0,6,8,3,1]
# print(Heuristic2(testPuz))