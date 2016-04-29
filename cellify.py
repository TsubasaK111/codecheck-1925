class Cell():
    def __init__(self, value, X, Y, x, y):
        self.X = int(X)
        self.Y = int(Y)
        self.x = int(x)
        self.y = int(y)
        self.value = int(value)
        if value != 0:
            self.constant = True


def cellify(grid):
    """Takes a sudoku grid (a recursive list of 3 items^4), and makes each
       item a 'cell' that can address where it is located in the grid"""
    for X, grid_row in enumerate(grid):
        for Y, subgrid in enumerate(grid_row):
            for x, row in enumerate(subgrid):
                for y, item in enumerate(row):
                    row[y] = Cell(value=item, X=X, Y=Y, x=x, y=y)
    return grid
