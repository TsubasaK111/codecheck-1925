import pdb, pprint

from matrixify import block_matrixify
from cellify import Cell, cellify
import testify

def solve(flat_array):
    print flat_array
    grids = []
    grid = block_matrixify(flat_array)
    grid = cellify(grid)
    grids.append(grid)
    solved_grid = testify.test_grid(grid)

    testify.print_grid(solved_grid)
    pdb.set_trace()
    return grid
