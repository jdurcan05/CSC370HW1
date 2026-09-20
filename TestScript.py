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
MAX_GENERATED = 100

generator = Puzzle.Puzzle()
finalData = {}
done = False
puzzles_generated = 0




for i in range(2,25):
    finalData[i] = []


while not done:
    done = True
    if puzzles_generated> MAX_GENERATED :
        break
    puzz = generator.generate()
    h2Struct = AStar.a_star(puzz,Heuristic2)
    if h2Struct[1]>24 or h2Struct[1]<2:
                done = False
                continue
    h1Struct = AStar.a_star(puzz,Heuristic1)
    h3Struct = AStar.a_star(puzz,Heuristic3)

    if h1Struct[1] == h2Struct[1] and h2Struct[1] == h3Struct[1]:
        g = h1Struct[1]
        finalData[g].append(Puzzledata(h1Struct[0],h2Struct[0],h3Struct[0]))
    else:
        exit("Something is wrong with a heuristic")
        print(h1Struct, h2Struct, h3Struct)
        print(puzz)

    puzzles_generated+=1
    
    for i in range(2,25):
        if(len(finalData[i])) < PUZZLES_WANTED:
            done = False
            break
    
for i in range(2,25):
    print(finalData[i])


# with open('Results.csv', mode='w', newline='', encoding='utf-8') as file:

#     header = ['Solution_number', 'Heuristic1', 'Heuristic2','Heuristic3']
#     file.writerow(header)

