import random

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

generator = Puzzle.Puzzle()
finalData = {}
done = False
puzzles_generated = 0
g = 2

states = generator.generate()


for i in range(2,26):
    finalData[i] = []


while g <= 24:
    matching_keys = [k for k, v in states.items() if v == g]
    if len(matching_keys) >= 100:
        random_keys = random.sample(matching_keys, 100)
    else:
        random_keys = matching_keys

    for puzz in random_keys:
        puzz = list(puzz)
        h1Struct = AStar.a_star(puzz,Heuristic1)
        h2Struct = AStar.a_star(puzz, Heuristic2)
        h3Struct = AStar.a_star(puzz,Heuristic3)

        if (h1Struct[1] == g or h1Struct[1] == g+1) and (g == h3Struct[1] or g+1 == h3Struct[1]):
            finalData[g].append(Puzzledata(h1Struct[0],h2Struct[0],h3Struct[0]))
        else:
            print(h1Struct, h2Struct, h3Struct)
            print(puzz)
            exit("Something is wrong with a heuristic")

    g+=2


actualData = {}

for i in range(2,26):
    if i%2 == 0:
        if not finalData[i]:
            continue
        actualData[i] = []
        h1AVG = 0
        h2AVG = 0
        h3AVG = 0
        for j in range(len(finalData[i])):
            h1AVG = h1AVG + finalData[i][j].h1Nodes
            h2AVG = h2AVG + finalData[i][j].h2Nodes
            h3AVG = h3AVG + finalData[i][j].h3Nodes
        h1AVG = h1AVG/len(finalData[i])
        h2AVG = h2AVG/len(finalData[i])
        h3AVG = h3AVG/len(finalData[i])
        actualData[i].append(i)
        actualData[i].append(h1AVG)
        actualData[i].append(h2AVG)
        actualData[i].append(h3AVG)
        actualData[i].append(len(finalData[i]))
        print(actualData[i])



with open("Results.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Solution Number",
        "Heuristic 1 Average Nodes",
        "Heuristic 2 Average Nodes",
        "Heuristic 3 Average Nodes",
        "Number of puzzles generated"
    ])

    for solution_number, averages in actualData.items():
        writer.writerow(averages)
