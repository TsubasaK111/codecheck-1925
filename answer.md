# Codecheck Sudoku[Python] Solution
   This is my solution for <a href="https://app.code-check.io/orgs/codecheck_official/challenges/109">Codecheck's Sudoku challenge</a> in Python.

##Methodology:
   This solution employs a simple backtracking algorithm with some modifications.
   * Sudoku grids are partitioned into <b>block matrixes</b> for better organization.
   * The entire 9x9 grid is named a '<b>grid</b>', and each 3x3 sub-matrix is a '<b>subgrid</b>'.
   * Each value is converted into a '<b>Cell</b>' object with coordinate values to
     simplify handling.
   * Each given value becomes a '<b>constant</b>' Cell to prevent being modified.
   * The algorithm begins from the top left-most Cell.
   * The target Cell, if not a given value, is enumerated through.
   * <b>Enumeration starts from the previous cell value + 1</b> to find a valid value faster.
   * For each enumerated attempt, tests are run to see if it is sudoku-valid.
   * If tests pass, then the algorithm recursively calls itself,
     passing in the partially solved grid and the next Cell in the grid.
   * If no enumerated attempt passes, the function ends returning nothing.
     (The current 'sub-tree' is pruned.)
   * When this tree reaches the last cell, then the grid is completely solved.
   * The solved grid is passed up the recursively created stack, up the tree,
     finally being returned to the top.

##Installation:
 1. **Install all requirements.**
 2. Download the contents of this repo to a directory of your choice.
 3. Open command prompt.
 4. Enter `cd [directory of your choice] && codecheck`
 5. `codecheck: tests  : 3  codecheck: success: 3` should print to console.
 6. This means that I'm moderately awesome. (And so are you!)

##Requirements:
 * <a href="https://www.python.org/downloads/">Python2</a>
 * <a href="https://docs.npmjs.com/getting-started/installing-node">Node.js/npm</a>
 * <a href="https://github.com/code-check/codecheck">Codecheck</a> ('npm install codecheck -g')
 * <a href="http://nose.readthedocs.io/en/latest/">Nosetests</a> ('pip install nose')

##License:
This repo is distributed under the <a href="http://opensource.org/licenses/MIT">MIT License</a>.

##Todo:
 * Refactor! Readability may be high, but this challenge can probably be solved with 1/10th the current amount of code.
 * Specifically, do not convert to a block matrix and solve the given matrix directly.
