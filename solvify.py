import pdb, sys
import testify
from matrixify import print_grid


def solve_grid(grid):
    global deepest_cell
    deepest_cell = grid[0][0][0][0]
    solved_grid = recursive_solve(grid[0][0][0][0], grid)
    return solved_grid


def recursive_solve(cell, grid):
    """Recursive backtracking algorithm component. Enumerate through integers in
       each cell and build solution candidates by recursively calling itself."""
    # prevent a bug where grids with a constant in last cell would not solve.
    if last_cell(cell) and cell.constant:
        return grid
    elif cell.constant:
        cell = next_cell(cell,grid)
    for i in range(1,10):
        cell = increment_cell(cell, grid)
        unique = testify.test_cell(cell, grid)
        if unique:
            # Test is a success, save value into cell and recurse to next cell
            save_cell(cell, grid)
            if last_cell(cell):
                # Tree has reached the last cell, so we have a solution grid!
                print_grid(grid)
                return grid
            else:
                solved_grid = recursive_solve(next_cell(cell, grid), grid)
                # if a solved grid is returned, send solved grid up the stack.
                if solved_grid is not None:
                    return solved_grid
    # this subtree does not have a solution, so it must be pruned (reset value).
    cell.value = 0
    save_cell(cell, grid)


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


def save_cell(cell, grid):
    """Method to save the given cell into the grid in the appropriate location.
       Also tracks depth of potential search tree to prevent solution
       corruption."""
    global deepest_cell
    current_node_depth = (((cell.X * 3 + cell.Y) * 3 + cell.x) * 3 + cell.y)
    deepest_node_depth = (((deepest_cell.X * 3 + deepest_cell.Y) * 3 + deepest_cell.x) * 3 + deepest_cell.y)
    if current_node_depth > deepest_node_depth:
        deepest_cell = cell
    # terminate if a solution has been reached
    # to prevent unsuccessful subtrees from corrupting.
    if last_cell(deepest_cell):
        return
    else:
        grid[cell.X][cell.Y][cell.x][cell.y] = cell


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
