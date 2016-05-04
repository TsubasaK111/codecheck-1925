class Cell():
    """Each sudoku number is managed as a 'Cell' to easily identify the
       location of each cell, and simplify deciding whether it is a given hint
       (aka a constant)or not."""
    def __init__(self, value, X=0, Y=0, x=0, y=0):
        # X and Y are coordinates in the whole sudoku grid for each subgrid.
        self.X = int(X)
        self.Y = int(Y)
        # x and y are coordinates in a 3x3 subgrid for each cell.
        self.x = int(x)
        self.y = int(y)
        self.initial_value = int(value)
        self.value = self.initial_value
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return """<Cell at Grid[{X}][{Y}][{x}][{y}] (value={value}, initial={initial})>""".format(
                value = self.value,
                initial = self.initial_value,
                X = self.X, Y = self.Y, x = self.x, y = self.y )


def cellify(grid):
    """Take a sudoku grid (a recursive list[4D] of items), and makes each
       item a 'Cell'."""
    for X, grid_column in enumerate(grid):
        for Y, subgrid in enumerate(grid_column):
            for x, column in enumerate(subgrid):
                for y, item in enumerate(column):
                    cell = Cell(value=item, X=X, Y=Y, x=x, y=y)
                    if cell.value != 0:
                        cell.constant = True
                    else:
                        cell.constant = False
                    column[y] = cell
    return grid


def uncellify(grid):
    """Reverse the 'cellify()' process and convert each Cell item into
       an integer in a sudoku grid."""
    for X, grid_column in enumerate(grid):
        for Y, subgrid in enumerate(grid_column):
            for x, column in enumerate(subgrid):
                for y, cell in enumerate(column):
                    column[y] = cell.value
    return grid


def increment_cell(cell, grid):
    """increment cell value based on the value of previous cell.
       this is to enable enumerating to a 'valid' value faster."""
    old_cell = previous_cell(cell, grid)
    if cell.value == 0:
        cell.value = old_cell.value + 1
    else:
        cell.value += 1
    if cell.value > 9:
        cell.value = 1
    return cell


def previous_cell(cell, grid):
    """Returns the previous cell in the grid."""
    X = cell.X
    Y = cell.Y
    x = cell.x
    y = cell.y
    y -= 1
    if y < 0:
        y = 0
        x -= 1
        if x < 0:
            x = 0
            Y -= 1
            if Y < 0:
                Y = 0
                X -= 1
                if X < 0:
                    # This is the first cell in the grid, so return first cell.
                    return cell
    old_cell = grid[X][Y][x][y]
    return old_cell


def next_cell(cell, grid):
    """Returns the next cell in the grid that is NOT a constant."""
    X = cell.X
    Y = cell.Y
    x = cell.x
    y = cell.y
    y += 1
    if y > 2:
        y = 0
        x += 1
        if x > 2:
            x = 0
            Y += 1
            if Y > 2:
                Y = 0
                X += 1
                if X > 2:
                    # This is the last cell in the grid, so return last cell.
                    return cell
    new_cell = grid[X][Y][x][y]
    # Find the next non-constant cell by recursion.
    if new_cell.constant == True:
        new_cell = next_cell(new_cell, grid)
    return new_cell


def last_cell(cell):
    if cell.X == 2 and cell.Y == 2 and cell.x ==2 and cell.y ==2:
        return True
    else:
        return False
