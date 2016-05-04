import pdb, sys


def test_cell(cell, grid):
    failed_tests=[]
    if (test_column(cell,grid) and test_row(cell,grid) and test_subgrid(cell,grid)):
        return True
    else:
        return False


def test_row(cell, grid):
    array = []
    for X, grid_column in enumerate(grid):
        for x, subgrid_column in enumerate(grid_column[cell.Y]):
            array.append(grid[X][cell.Y][x][cell.y])
    return test_array(array, cell)

def test_column(cell, grid):
    array = []
    for Y, subgrid in enumerate(grid[cell.X]):
        for y, row in enumerate(subgrid[cell.x]):
            array.append(grid[cell.X][Y][cell.x][y])
    return test_array(array, cell)

def test_subgrid(cell, grid):
    array = []
    for x, subgrid_column in enumerate(grid[cell.X][cell.Y]):
        for y, other_cell in enumerate(subgrid_column):
            array.append(grid[cell.X][cell.Y][x][y])
    return test_array(array, cell)

def test_array(array, cell):
    if cell.constant:
        raise ValueError("Cell value is constant!!", cell, array)
    elif cell.value == 0:
        raise ValueError("Cell value is zero!", cell, array)
    # create new array containing only cell values so
    # .count method can be used to identify overlapping values in array.
    value_array = []
    for other_cell in array:
        value_array.append(other_cell.value)
    if value_array == []:
        found = 0
    else:
        found = value_array.count(cell.value)
    if found > 1:
        return False
    else:
        return True
