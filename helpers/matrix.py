def block_matrixify(flat_array):
    """Restructure the two-dimensional array into four-dimensions
       (a matrix of a matrices)"""

    block_matrix = [[[[0 for y in range(3)] for x in range(3)]
                   for Y in range(3)] for X in range(3)]

    for A, column in enumerate(flat_array):
        for b, item in enumerate(column):
            X = int( A / 3 )
            Y = int( b / 3 )
            x = ( A % 3 )
            y = ( b % 3 )
            block_matrix[X][Y][x][y] = item
    return block_matrix

def un_block_matrixify(block_matrix):
    """Reverse the 'block_matrixify()' process and restructure the
       four-dimensional array into a two-dimensional array"""
    flat_array = [[0 for b in range(9)] for A in range(9)]
    for X, grid_column in enumerate(block_matrix):
        for Y, subgrid in enumerate(grid_column):
            for x, column in enumerate(subgrid):
                for y, item in enumerate(column):
                    A = (X * 3) + x
                    b = (Y * 3) + y
                    flat_array[A][b] = item
    return flat_array


def print_grid(grid):
    """Prettily print a sudoku grid."""
    print "-----------------------"
    for Y in range(3):
        for y in range(3):
            output = "["
            for X in range(3):
                output += "[ "
                for x in range(3):
                    try:
                        output += str(grid[X][Y][x][y].value)
                    except:
                        output += "*" + str(grid[X][Y][x][y])
                output += " ]"
            output += "]"
            print output
        print "-----------------------"
