# Information

Sudoku is a number-placement puzzle.

The goal of this challenge is to write a sudoku solving algorithm.

## Step 1. Solve sudoku

The application will send you 3 different puzzles in the form of two-dimensional arrays.

Solve these puzzles in the "solve" function.

## Step 2. Explain your code
In [answer.md](./answer.md) write a brief explanation about how your code works and how you solved any problems that you encountered.

## Notes
### About Python
- The test is run using `nosetests`.
- The Python version is 2.x. (TestServer uses 2.7.6)

- With codecheck, you can run the test code and confirm whether your answer is correct.
- If you are taking the test via the Codecheck Web Editor, hit the "Run" button in the console.
- If you are taking the test locally via GitHub, follow these instructions to install the Codecheck CLI and run the tests.

- Go to the root folder in your cloned project, and install Codecheck CLI with the below command:
```
$ npm install codecheck -g
```

- To run the test, enter `codecheck` from the root folder.


### Sudoku rules

Sudoku is a puzzle made out of a 9x9 matrix. The matrix is made of 9 sub-grids which are made of 3x3 cells.
A valid sudoku contains the numbers 1-9 each 9 times while not breaking one simple rule: "A sub-grid, column or row can only contain each number once".

You can find more details on [Wikipedia](https://en.wikipedia.org/wiki/Sudoku).

### Sudoku solution

Some sudoku have multiple solutions, but all of the puzzles we provide have a unique solution.

#### Puzzle 1

<table><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>9</td><td>8</td><td>&nbsp;</td><td>5</td><td>1</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>5</td><td>1</td><td>9</td><td>&nbsp;</td><td>7</td><td>4</td><td>2</td><td>&nbsp;</td></tr><tr><td>2</td><td>9</td><td>&nbsp;</td><td>4</td><td>&nbsp;</td><td>1</td><td>&nbsp;</td><td>6</td><td>5</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>1</td><td>4</td><td>&nbsp;</td><td>5</td><td>&nbsp;</td><td>8</td><td>&nbsp;</td><td>9</td><td>3</td></tr><tr><td>&nbsp;</td><td>2</td><td>6</td><td>7</td><td>&nbsp;</td><td>9</td><td>5</td><td>8</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>5</td><td>1</td><td>&nbsp;</td><td>3</td><td>6</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr></table>

#### Puzzle 2

<table><tr><td>&nbsp;</td><td>&nbsp;</td><td>3</td><td>&nbsp;</td><td>2</td><td>&nbsp;</td><td>6</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>9</td><td>&nbsp;</td><td>&nbsp;</td><td>3</td><td>&nbsp;</td><td>5</td><td>&nbsp;</td><td>&nbsp;</td><td>1</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>1</td><td>8</td><td>&nbsp;</td><td>6</td><td>4</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>8</td><td>1</td><td>&nbsp;</td><td>2</td><td>9</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>7</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>8</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>6</td><td>7</td><td>&nbsp;</td><td>8</td><td>2</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>2</td><td>6</td><td>&nbsp;</td><td>9</td><td>5</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>8</td><td>&nbsp;</td><td>&nbsp;</td><td>2</td><td>&nbsp;</td><td>3</td><td>&nbsp;</td><td>&nbsp;</td><td>9</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>5</td><td>&nbsp;</td><td>1</td><td>&nbsp;</td><td>3</td><td>&nbsp;</td><td>&nbsp;</td></tr></table>

#### Puzzle 3

<table><tr><td>9</td><td>&nbsp;</td><td>4</td><td>2</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>7</td></tr><tr><td>&nbsp;</td><td>1</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>7</td><td>&nbsp;</td><td>6</td><td>5</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>8</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>9</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>2</td><td>&nbsp;</td><td>9</td><td>&nbsp;</td><td>4</td><td>&nbsp;</td><td>6</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>4</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>2</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>1</td><td>6</td><td>&nbsp;</td><td>7</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>3</td><td>&nbsp;</td></tr><tr><td>3</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>5</td><td>7</td><td>&nbsp;</td><td>2</td></tr></table>
