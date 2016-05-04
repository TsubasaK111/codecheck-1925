import pdb, sys
import testify
from matrixify import print_grid
from cellify import increment_cell, previous_cell, next_cell, last_cell


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
        success = testify.test_cell(cell, grid)
        if success:
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
