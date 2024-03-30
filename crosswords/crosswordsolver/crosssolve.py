from crosswords.crosswordsolver.solver.BPSolver import BPSolver
from crosswords.crosswordsolver.solver.Crossword import Crossword
from crosswords.crosswordsolver.solver.Utils import convert_puz
from crosswords.crosswordsolver.solver.Utils import print_grid
from db.db import db
import json
import os
import re

puzzle_file = './puzzles/LA_times/20240301.puz'

def cross(puzzle_file):

    def solve(crossword):
        solver = BPSolver(crossword, max_candidates=500000)
        solution = solver.solve(num_iters=10, iterative_improvement_steps=5)
        print("* Solver Output *")
        print(solution)
        print_grid(solution)
        print("* Gold Solution *")
        print_grid(crossword.letter_grid)
        solver.evaluate(solution)
        return solution

    uploaded_puzzles = db['user-uploaded-puzzles']
 
    puzzle = convert_puz(puzzle_file)
    print(type(puzzle))
    print(puzzle)
    result = uploaded_puzzles.insert_one(puzzle)
    crossword = Crossword(puzzle)
    solution = solve(crossword)
    return solution
