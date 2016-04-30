import pdb;


def print_grid(grid):
    for X, grid_row in enumerate(grid):
        for x in range(0,3):
            output = "["
            for Y in range(0,3):
                output += "[ "
                for y in range(0,3):
                    output += str(grid[X][Y][x][y].value)
                output += " ]"
            output = output + "]"
            print output


def increment(cell):
    cell.value = cell.value + 1
    if cell.value > 9:
        cell.value = 1
    return cell


def test_grid(grid):
    for X, grid_row in enumerate(grid):
        for Y, subgrid in enumerate(grid_row):
            for x, subgrid_row in enumerate(subgrid):
                for y, cell in enumerate(subgrid_row):
                    subgrid_row[y] = try_something(cell, grid)
    return grid



def try_something(cell, grid):
    if cell.constant:
        return cell
    elif cell.value == 0:
        cell = increment(cell)

    try:
        unique, failed_tests = test_cell(cell, grid)
    except ValueError as error:
        pdb.set_trace()

    if not unique:
        for i in range(1,9):
            cell = increment(cell)
            unique, failed_tests = test_cell(cell, grid)
            if unique:
                return cell
        if not unique:
            print "backtrack!", failed_tests, cell
            print_grid(grid)
            pdb.set_trace()
            #TODO: implement recursive backtracking
    return cell


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
    # if cell.Y ==1 and cell.value==5:
    #     pdb.set_trace()
    if cell.constant:
        raise ValueError("Cell value is constant!!", cell, array)
    elif cell.value == 0:
        raise ValueError("Cell value is zero!", cell, array)
    # create new array containing only cell values so
    # .count method can be used to identify overlapping values in array.
    value_array = []
    for other_cell in array:
        value_array.append(other_cell.value)
    found = value_array.count(cell.value)
    if found > 1:
        return False
    else:
        return True
