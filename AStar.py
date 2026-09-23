import Puzzle.Heuristics
from Puzzle.PuzzleFunctions import *
from Puzzle.Heuristics import Heuristic1, Heuristic2, Heuristic3 # for testing

import heapq

def a_star(puzzle, heuristic):
    pq = []
    visited = set()
    generated = set()
    counter = 0 # for pq tie breakers
    heapq.heappush(pq, (heuristic(puzzle), counter, puzzle, 0))

    current_num = ""
    for i in range(0,9):
        current_num = current_num + str(puzzle[i])
    generated.add(current_num)

    while 1:
        _, _, current, g = heapq.heappop(pq)

        current_num = ""
        for i in range(0,9):
            current_num = current_num + str(current[i])
        if current_num in visited:
            continue
        visited.add(current_num)

        if isCompleted(current):
            return (counter, g)

        states = []
        states.extend(returnPermutations(current))
        for state in states:

            #Check for duplicate node generation
            current_num = ""
            for i in range(0,9):
                current_num = current_num + str(state[i])

            if current_num not in generated:
                counter += 1
                generated.add(current_num)
            
            heapq.heappush(pq,(heuristic(state) + g, counter, state, g + 1))