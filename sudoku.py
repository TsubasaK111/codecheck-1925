import pdb, pprint

from matrixify import block_matrixify, un_block_matrixify
from cellify import Cell, cellify, uncellify
from solvify import solve_grid

def solve(flat_array):
    print flat_array
    grid = block_matrixify(flat_array)
    grid = cellify(grid)
    solved_grid = solve_grid(grid)
    grid = uncellify(grid)
    solved_flat_array = un_block_matrixify(grid)
    print flat_array
    print solved_flat_array
    return solved_flat_array
