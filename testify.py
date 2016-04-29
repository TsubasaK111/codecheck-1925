import pdb


def increment(cell):
    if cell.constant:
        raise ValueError("Cell value is constant!", cell)
        return cell

    cell.value = cell.value + 1
    if cell.value > 9:
        cell.value = 1
    return cell


def try_something(cell, grid):
    if cell.constant:
        return
    elif cell.value == 0:
        cell = increment(cell)
        #false here...
    try:
        unique = test_cell(cell, grid)
    except ValueError as error:
        return

    if not unique:
        for i in range(1,9):
            cell = increment(cell)
            unique = test_cell(cell, grid)
            if unique:
                break
        if not unique:
            print "backtrack!"
            pdb.set_trace()


def test_cell(cell, grid):

    def test_column(cell):
        array = []
        for X, grid_row in enumerate(grid):
            for x, subgrid_row in enumerate(grid_row[cell.Y]):
                array.append(grid[X][cell.Y][x][cell.y])
        return test_array(array, cell)

    def test_row(cell):
        array = []
        for Y, subgrid in enumerate(grid[cell.X]):
            for y, column in enumerate(subgrid[cell.x]):
                array.append(grid[cell.X][Y][cell.x][y])
        return test_array(array, cell)

    def test_subgrid(cell):
        array = []
        for x, subgrid_row in enumerate(grid[cell.X][cell.Y]):
            for y, cell in enumerate(subgrid_row):
                array.append(grid[cell.X][cell.Y][x][y])
        return test_array(array, cell)

    def test_array(array, cell):
        if cell.constant:
            raise ValueError("Cell value is constant!!", cell, array)
        elif cell.value == 0:
            raise ValueError("Cell value is zero!", cell, array)
        found = array.count(cell.value)
        if found > 1:
            return False
        else:
            return True

    if test_column(cell) and test_row(cell) and test_subgrid(cell):
        return True
    else:
        return False


def test_grid(grid):
    for X, grid_row in enumerate(grid):
        for Y, subgrid in enumerate(grid_row):
            for x, subgrid_row in enumerate(subgrid):
                for y, cell in enumerate(subgrid_row):
                    result = try_something(cell, grid)
