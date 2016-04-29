import pdb


def block_matrixify(flat_array):
    """Restructure the two-dimensional array into four-dimensions
       (a matrix of a matrices)"""

    block_matrix = [[[[0 for a in range(3)] for b in range(3)]
                   for a in range(3)] for b in range(3)]

    for B, column in enumerate(flat_array):
        for a, item in enumerate(column):
            X = int( a / 3 )
            Y = int( B / 3 )
            x = ( a % 3 )
            y = ( B % 3 )
            print """assigning {item} to block_matrix[{X}][{Y}][{x}][{y}]...
                  """.format( item = item, X = X, Y = Y, x = x, y = y )
            block_matrix[X][Y][x][y] = item

    return block_matrix
