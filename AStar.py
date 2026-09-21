import Puzzle.Heuristics
from Puzzle.PuzzleFunctions import *
from Puzzle.Heuristics import Heuristic1, Heuristic2, Heuristic3 # for testing

import heapq

def a_star(puzzle, heuristic):
    pq = []
    visited = set()
    counter = 0 # for pq tie breakers
    heapq.heappush(pq, (heuristic(puzzle), counter, puzzle, 1))

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
            counter += 1
            heapq.heappush(pq,(heuristic(state) + g, counter, state, g + 1))

if __name__ == "__main__":
    test_board = [8,7,6,5,4,3,2,1,0]
    print(a_star(test_board, Puzzle.Heuristics.Heuristic1))