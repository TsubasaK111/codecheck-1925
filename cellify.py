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
