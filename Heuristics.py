from Puzzle.PuzzleFunctions import checkInput

def Heuristic1(puzzle):
    checkInput(puzzle)
    hVal = 0
    #Currently uncertain about the 0 in the puzzle, will ask Dr. R about that today
    for i in range(1, len(puzzle)):
        if i != puzzle[i]:
            hVal = hVal + 1
    return hVal





def Heuristic2():
    return None


testPuz = [1,0,2,3,4,5,6,8,7]

print(Heuristic1(testPuz))