import pdb


def block_matrixify(flat_array):
    """Restructure the two-dimensional array into four-dimensions
       (a matrix of a matrices)"""

    block_matrix = [[[[0 for a in range(3)] for b in range(3)]
                   for c in range(3)] for d in range(3)]

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

def un_block_matrixify(block_matrix):
    """Reverse the 'block_matrixify()' process and restructure the
       four-dimensional array into a two-dimensional array"""
    flat_array = [[0 for a in range(9)] for B in range(9)]

    for X, grid_row in enumerate(block_matrix):
        for Y, subgrid in enumerate(grid_row):
            for x, row in enumerate(subgrid):
                for y, item in enumerate(row):
                    B = (X * 3) + x
                    a = (Y * 3) + y
                    print """assigning {item} to flat_array[{B}][{a}]...
                          """.format( item = item, B = B, a = a)
                    flat_array[B][a] = item
