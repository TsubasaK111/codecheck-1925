import pdb, pprint
import numpy


class Cell():
    def __init__(self, value, X, Y, x, y):
        self.X = int(X)
        self.Y = int(Y)
        self.x = int(x)
        self.y = int(y)
        self.value = int(value)
        if value != 0:
            self.constant = True

def gridify(flat_array):
    """Takes a flat_array of 9 items and fits them into a 3x3 list of lists"""
    # Creates a list containing 3 lists, each of 3 cells, all set to 0
    grid = [[0 for a in range(3)] for b in range(3)]
    x, y = 0, 0

    # Takes flat array and fits
    for i, item in enumerate(flat_array):
        grid[x][y] = item
        x += 1
        if (i + 1) % 3 == 0:
            x = 0
            y += 1
        elif (i+1) == 9:
            print grid
            return grid
    return grid


def cellify(grid):
    for X, grid_row in enumerate(grid):
        for Y, subgrid in enumerate(grid_row):
            for x, row in enumerate(subgrid):
                for y, item in enumerate(row):
                    item = Cell(value=item, X=X, Y=Y, x=x, y=y)
    return grid

def solve(flat_array):

    grid = flat_array
    # First, restructure the two-dimensional array into four-dimensions
    for i, subgrid in enumerate(grid):
        grid[i] = gridify(subgrid)
    grid = gridify(grid)

    # TODO: ^^This is unelegant, functionalize and abstract away the above!^^

    grid = cellify(grid)
    pdb.set_trace()

    return grid

def test_grid(grid):
    for X, grid_row in enumerate(grid):
        for Y, subgrid in enumerate(grid_row):
            for x, row in enumerate(subgrid):
                for y, cell in enumerate(row):
                    test_cell(cell)

def test_cell(cell):
    pdb.set_trace()
    if test_for_column and test_for_row and test_for_subgrid:
        print cell

def test_for_column(cell):
    pdb.set_trace()
    return true

def test_for_row(cell):
    return true

def test_for_subgrid(cell):
    return true
