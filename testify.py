import pdb


def test_array(array, cell):
    found = array.count(cell.value)
    if found > 1:
        return false
    else:
        return True


def test_grid(grid):

    def test_cell(cell):
        if test_column(cell) and test_row(cell) and test_subgrid(cell):
            return True
        else:
            return False

    def test_column(cell):
        array = []
        for X, grid_row in enumerate(grid):
            for x, subgrid_row in enumerate(grid_row[cell.Y]):
                array.append(grid[X][cell.Y][x][cell.y])
        return test_array(array, cell)

    def test_row(cell):
        array = []
        for Y, subgrid in enumerate(grid[cell.X]):
            for y, column in enumerate(grid_row[cell.x]):
                array.append(grid[cell.X][Y][cell.x][y])
        return test_array(array, cell)

    def test_subgrid(cell):
        array = []
        for x, subgrid_row in enumerate(grid[cell.X][cell.Y]):
            for y, cell in enumerate(subgrid_row):
                array.append(grid[cell.X][cell.Y][x][y])
        return test_array(array, cell)


    for X, grid_row in enumerate(grid):
        for Y, subgrid in enumerate(grid_row):
            for x, subgrid_row in enumerate(subgrid):
                for y, cell in enumerate(subgrid_row):
                    if test_cell(cell):
                        print str(cell.value) + " is True!"
                    else:
                        print str(cell.value) + " is False!"
