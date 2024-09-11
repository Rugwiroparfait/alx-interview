# 0x05. N Queens - Algorithm Project

## Overview
This project is focused on solving the classic N Queens puzzle using Python. The N Queens puzzle is a well-known problem in mathematics and computer science that involves placing N non-attacking queens on an N×N chessboard. The project requires the use of backtracking algorithms to explore and find all possible solutions.

## Concepts Needed
To succeed in this project, you will need to understand the following key concepts:

- **Backtracking Algorithms**: A strategy for finding all (or some) solutions by trying partial solutions and then abandoning them if they are not successful.
- **Recursion**: Recursively implementing the backtracking algorithm to explore potential queen placements.
- **List Manipulations**: Storing and updating the positions of queens on the chessboard using lists.
- **Command Line Arguments**: Using the `sys` module to handle command-line inputs in Python.

### Helpful Resources:
- [Backtracking Introduction](https://www.geeksforgeeks.org/backtracking-algorithms/)
- [Recursion in Python](https://realpython.com/python-recursion/)
- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)
- [Command Line Arguments in Python](https://docs.python.org/3/library/sys.html#sys.argv)

## Requirements

- **General**:
  - Your code should be written in **Python 3**.
  - Use any allowed editors like `vi`, `vim`, or `emacs`.
  - Files will be interpreted on Ubuntu 20.04 LTS.
  - All files should follow PEP 8 coding standards.
  - Include a `README.md` file in the project directory.
  - All files must be executable and should end with a newline.
  - You can only import the `sys` module for this task.

## Task - 0. N Queens
### Challenge
The objective is to write a program that solves the N Queens puzzle, which involves placing N queens on an N×N chessboard such that no two queens threaten each other.

### Usage
```bash
./0-nqueens.py N
```

- **N**: The size of the chessboard, must be an integer greater than or equal to 4.
  
### Constraints:
1. If the program is called with an incorrect number of arguments, print:
   ```bash
   Usage: nqueens N
   ```
   and exit with status code 1.

2. If **N** is not an integer, print:
   ```bash
   N must be a number
   ```
   and exit with status code 1.

3. If **N** is less than 4, print:
   ```bash
   N must be at least 4
   ```
   and exit with status code 1.

### Output:
- The program should print every possible solution to the N Queens problem.
- Each solution should be printed as a list of queen positions. For example, the solution for **N = 4** is:
  ```bash
  [[0, 1], [1, 3], [2, 0], [3, 2]]
  [[0, 2], [1, 0], [2, 3], [3, 1]]
  ```
- There is no need to print the solutions in a specific order.

### Example Usage:
```bash
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

## File Structure
```bash
├── 0-nqueens.py
└── README.md
```

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/alx-interview.git
   ```
2. Navigate to the project directory:
   ```bash
   cd 0x05-nqueens
   ```
3. Run the program with the size of the chessboard (N):
   ```bash
   ./0-nqueens.py N
   ```

## Author
Rugwiro Parfait
