class Cell():
    def __init__(self, value, X=0, Y=0, x=0, y=0):
        self.X = int(X)
        self.Y = int(Y)
        self.x = int(x)
        self.y = int(y)
        self.initial_value = int(value)
        self.value = self.initial_value
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return """<Cell at Grid[{X}][{Y}][{x}][{y}] (value={value}, initial={initial_value})>""".format(
                value = self.value,
                initial_value = self.initial_value,
                X = self.X,
                Y = self.Y,
                x = self.x,
                y = self.y )


def cellify(grid):
    """Take a sudoku grid (a recursive list of 3 items^4), and makes each
       item a 'cell' that can address where it is located in the grid"""
    for X, grid_row in enumerate(grid):
        for Y, subgrid in enumerate(grid_row):
            for x, row in enumerate(subgrid):
                for y, item in enumerate(row):
                    cell = Cell(value=item, X=X, Y=Y, x=x, y=y)
                    if cell.value != 0:
                        cell.constant = True
                    else:
                        cell.constant = False
                    row[y] = cell
    return grid

def uncellify(grid):
    """Reverse the 'cellify()' process and convert each Cell item into
       an integer in a sudoku grid."""
    for X, grid_row in enumerate(grid):
        for Y, subgrid in enumerate(grid_row):
            for x, row in enumerate(subgrid):
                for y, cell in enumerate(row):
                    row[y] = cell.value
    return grid
