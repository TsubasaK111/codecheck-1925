import pdb, pprint

from matrixify import block_matrixify, un_block_matrixify
from cellify import Cell, cellify, uncellify
import solvify

def solve(flat_array):
    print flat_array
    grid = block_matrixify(flat_array)
    grid = cellify(grid)
    solved_grid = solvify.solve_grid(grid)
    solvify.print_grid(solved_grid)
    pdb.set_trace()
    grid = uncellify(grid)
    flat_array = un_block_matrixify(grid)
    pdb.set_trace()
    return grid
