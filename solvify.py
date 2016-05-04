import pdb, sys
import testify
from matrixify import print_grid


def solve_grid(grid):
    global deepest_cell
    deepest_cell = grid[0][0][0][0]
    solved_grid = recursive_solve(grid[0][0][0][0], grid)
    return solved_grid

def increment_cell(cell, grid):
    # pdb.set_trace()
    old_cell = previous_cell(cell, grid)
    if cell.value == 0:
        cell.value = old_cell.value + 1
    else:
        cell.value += 1
    if cell.value > 9:
        cell.value = 1
    return cell

def recursive_solve(cell, grid):
    if last_cell(cell) and cell.constant:
        return grid
    elif cell.constant:
        print "cell is constant!"
        cell = next_cell(cell,grid)
    for i in range(1,10):
        cell = increment_cell(cell, grid)
        unique = testify.test_cell(cell, grid)
        if unique:
            # Test is a success, save successful value into cell, move to next cell
            save_cell(cell, grid)
            print "cell value set to: " + cell.__repr__()
            if last_cell(cell):
                print "I think we have a winner!!! :D"
                print_grid(grid)
                # pdb.set_trace()
                return grid
            else:
                solved_grid = recursive_solve(next_cell(cell, grid), grid)
                if solved_grid is not None:
                    print "returning solved grid up the recursive stack..."
                    return solved_grid
                print "backtracking..."
    print "end of the line for this cell!"
    cell.value = 0
    save_cell(cell, grid)
    print_grid(grid)
    print cell.__repr__()


def save_cell(cell, grid):
    global deepest_cell
    current_node_depth = (((cell.X * 3 + cell.Y) * 3 + cell.x) * 3 + cell.y)
    deepest_node_depth = (((deepest_cell.X * 3 + deepest_cell.Y) * 3 + deepest_cell.x) * 3 + deepest_cell.y)
    if current_node_depth > deepest_node_depth:
        deepest_cell = cell
    if last_cell(deepest_cell):
        return
    else:
        grid[cell.X][cell.Y][cell.x][cell.y] = cell


def last_cell(cell):
    if cell.X == 2 and cell.Y == 2 and cell.x ==2 and cell.y ==2:
        return True
    else:
        return False

def previous_cell(cell, grid):
    print "cell is: ", cell.__repr__()
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
                    return cell
    old_cell = grid[X][Y][x][y]
    print "previous cell is: ", old_cell.__repr__()
    return old_cell

def next_cell(cell, grid):
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
                    return cell
    new_cell = grid[X][Y][x][y]
    if new_cell.constant == True:
        print "cell is constant!"
        new_cell = next_cell(new_cell, grid)
    print "next up: ", new_cell.__repr__()
    return new_cell
