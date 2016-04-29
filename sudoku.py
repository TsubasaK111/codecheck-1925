import pdb, pprint

from matrixify import block_matrixify
from cellify import Cell, cellify
import testify

def solve(flat_array):
    print flat_array
    grid = block_matrixify(flat_array)
    grid = cellify(grid)
    testify.test_grid(grid)
    pdb.set_trace()
    return grid

def print_grid(grid):
    for X, grid_row in enumerate(grid):
        for Y, subgrid in enumerate(grid_row):
            for x, subgrid_row in enumerate(subgrid):
                for y, item in enumerate(subgrid_row):
                    print item
