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

