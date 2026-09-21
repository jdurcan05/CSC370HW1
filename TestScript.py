from Puzzle.Heuristics import Heuristic1, Heuristic2, Heuristic3 # for testing
from Puzzle.PuzzleFunctions import *
from Puzzle import Puzzle
import AStar
import csv
from dataclasses import dataclass

@dataclass 
class Puzzledata:
    h1Nodes: int
    h2Nodes: int
    h3Nodes: int

PUZZLES_WANTED = 1
MAX_GENERATED = 20000000000000,

generator = Puzzle.Puzzle()
finalData = {}
done = False
puzzles_generated = 0




for i in range(2,26):
    finalData[i] = []


while not done:
    done = True
    if puzzles_generated> MAX_GENERATED :
        break
    puzz = generator.generate()
    h2Struct = AStar.a_star(puzz,Heuristic2)
    if h2Struct[1]%2 == 1:
        g = h2Struct[1]-1
    else:
        g = h2Struct[1]
    if g>24 or g<2 or len(finalData[g]) >= PUZZLES_WANTED:
        puzzles_generated+=1
        done = False
        continue
    h1Struct = AStar.a_star(puzz,Heuristic1)
    h3Struct = AStar.a_star(puzz,Heuristic3)

    if (h1Struct[1] == g or h1Struct[1] == g+1) and (g == h3Struct[1] or g+1 == h3Struct[1]):
        g = h1Struct[1]
        finalData[g].append(Puzzledata(h1Struct[0],h2Struct[0],h3Struct[0]))
    else:
        print(h1Struct, h2Struct, h3Struct)
        print(puzz)
        exit("Something is wrong with a heuristic")

    puzzles_generated+=1
    
    for i in range(2,26):
        if i%2 == 0:
            if(len(finalData[i])) < PUZZLES_WANTED:
                done = False
                break
    
for i in range(2,26):
    if i%2 == 0:
        print(finalData[i])


# with open('Results.csv', mode='w', newline='', encoding='utf-8') as file:

#     header = ['Solution_number', 'Heuristic1', 'Heuristic2','Heuristic3']
#     file.writerow(header)

