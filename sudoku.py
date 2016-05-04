import pdb, pprint

from matrixify import block_matrixify, un_block_matrixify
from cellify import Cell, cellify, uncellify
from solvify import solve_grid

def solve(flat_array):
    print "input is: " + str(flat_array)
    grid = block_matrixify(flat_array)
    grid = cellify(grid)
    solved_grid = solve_grid(grid)
    solved_grid = uncellify(solved_grid)
    solved_flat_array = un_block_matrixify(solved_grid)
    return solved_flat_array
