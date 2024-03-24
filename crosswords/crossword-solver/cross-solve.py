from solver.BPSolver import BPSolver
from solver.Crossword import Crossword
from solver.Utils import convert_puz
from solver.Utils import print_grid
import json
import os
import re

puzzle_file = './data/LA_times/20240310.puz'


def solve(crossword):
    solver = BPSolver(crossword, max_candidates=500000)
    solution = solver.solve(num_iters=10, iterative_improvement_steps=5)
    print("* Solver Output *")
    print(solution)
    print_grid(solution)
    print("* Gold Solution *")
    print_grid(crossword.letter_grid)
    solver.evaluate(solution)
    date_part = re.search(r'(\d{8})', puzzle_file).group()
    crossword_data = {"answers": solution}
    existing_folder_path = "./data/LA_times/answers/"
    file_path = os.path.join(existing_folder_path, f'{date_part}.json')
    with open(file_path, 'w') as json_file:
        json.dump(crossword_data, json_file)
    print(f"Crossword solution has been saved to {file_path}")


puzzle = convert_puz(puzzle_file)
print(puzzle)
crossword = Crossword(puzzle)
solve(crossword)
