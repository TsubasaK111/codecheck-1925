import pdb, pprint

from matrixify import block_matrixify
from cellify import Cell, cellify
import testify

def solve(flat_array):
    print flat_array
    grid = block_matrixify(flat_array)
    grid = cellify(grid)
    testify.test_grid(grid)
    print_grid(grid)
    pdb.set_trace()
    return grid

def print_grid(grid):
    for X, grid_row in enumerate(grid):
        for x in range(0,2):
            print ( grid[X][0][x][0], grid[X][0][x][1], grid[X][0][x][2],
                    grid[X][1][x][0], grid[X][1][x][1], grid[X][1][x][2],
                    grid[X][2][x][0], grid[X][2][x][1], grid[X][2][x][2] )
