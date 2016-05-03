import pdb, sys
import testify


def print_grid(grid):
    try:
        print "#########"
        for X, grid_row in enumerate(grid):
            for x in range(0,3):
                output = "["
                for Y in range(0,3):
                    output += "[ "
                    for y in range(0,3):
                        try:
                            output += str(grid[X][Y][x][y].value)
                        except:
                            output += "*" + str(grid[X][Y][x][y])
                    output += " ]"
                output = output + "]"
                print output
    except: # catch *all* exceptions
        error = sys.exc_info()[0]
        pdb.set_trace()


def solve_grid(grid):


    def save_cell(cell):
        global deepest_cell
        grid[cell.X][cell.Y][cell.x][cell.y] = cell
        current_node_depth = (((cell.X * 3 + cell.Y) * 3 + cell.x) * 3 + cell.y)
        deepest_node_depth = (((deepest_cell.X * 3 + deepest_cell.Y) * 3 + deepest_cell.x) * 3 + deepest_cell.y)
        if current_node_depth > deepest_node_depth:
            deepest_cell = cell


    def recursive_solve(cell):
        try:
            if cell.constant:
                print "cell is constant!"
                cell = next_cell(cell,grid)

            for i in range(1,10):
                cell.value = i
                unique, failed_tests = testify.test_cell(cell, grid)
                if unique:
                    # Test is a success!
                    # Store successful value into cell and move to next cell
                    save_cell(cell)
                    print "cell value set to: " + cell.__repr__()
                    if cell.X == 2 and cell.Y == 2 and cell.x ==2 and cell.y ==2:
                        print "I think we have a winner!!! :D"
                        print_grid(grid)
                        pdb.set_trace()
                        return grid
                    else:
                        recursive_solve(next_cell(cell, grid))
                        print "backtrack!"

            print "end of the line for this cell!"
            cell.value = 0
            save_cell(cell)
            print_grid(grid)
            print cell.__repr__()

        except: # catch *all* exceptions
            error = sys.exc_info()[0]
            pdb.set_trace()

    global deepest_cell
    deepest_cell = grid[0][0][0][0]

    recursive_solve(grid[0][0][0][0])
    print "deepest node was at: " + deepest_cell.__repr__()
    pdb.set_trace()
    return grid



def next_cell(cell, grid):
    try:
        print "cell was: ", cell.__repr__()
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
                        pdb.set_trace()
        new_cell = grid[X][Y][x][y]
        if new_cell.constant == True:
            print "cell is constant!"
            new_cell = next_cell(new_cell, grid)
        print "next up: ", new_cell.__repr__()
        return new_cell
    except: # catch *all* exceptions
        error = sys.exc_info()[0]
        pdb.set_trace()
