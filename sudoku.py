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
    grid = uncellify(grid)
    solved_flat_array = un_block_matrixify(grid)
    print flat_array
    print solved_flat_array
    pdb.set_trace()
    return solved_flat_array
