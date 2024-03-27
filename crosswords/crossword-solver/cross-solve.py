from solver.BPSolver import BPSolver
from solver.Crossword import Crossword
from solver.Utils import convert_puz
from solver.Utils import print_grid
import json
import os
import re

puzzle_file = './puzzles/LA_times/20240310.puz'


def solve(crossword):
    solver = BPSolver(crossword, max_candidates=500000)
    solution = solver.solve(num_iters=10, iterative_improvement_steps=5)
    print("* Solver Output *")
    print(solution)
    print_grid(solution)
    print("* Gold Solution *")
    print_grid(crossword.letter_grid)
    solver.evaluate(solution)


puzzle = convert_puz(puzzle_file)
print(puzzle)
crossword = Crossword(puzzle)
solve(crossword)
