import pdb, sys


def test_cell(cell, grid):
    failed_tests=[]
    unique = True
    if not test_column(cell,grid):
        failed_tests.append('test_column')
        unique = False
    if not test_row(cell,grid):
        failed_tests.append('test_row')
        unique = False
    if not test_subgrid(cell,grid):
        failed_tests.append('test_subgrid')
        unique = False
    return unique, failed_tests


def test_column(cell, grid):
    array = []
    for X, grid_row in enumerate(grid):
        for x, subgrid_row in enumerate(grid_row[cell.Y]):
            array.append(grid[X][cell.Y][x][cell.y])
    return test_array(array, cell)

def test_row(cell, grid):
    array = []
    for Y, subgrid in enumerate(grid[cell.X]):
        for y, column in enumerate(subgrid[cell.x]):
            array.append(grid[cell.X][Y][cell.x][y])
    return test_array(array, cell)

def test_subgrid(cell, grid):
    array = []
    for x, subgrid_row in enumerate(grid[cell.X][cell.Y]):
        for y, other_cell in enumerate(subgrid_row):
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
