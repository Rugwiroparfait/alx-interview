# 0x09. Island Perimeter

## Project Overview

This project is designed to test your understanding of algorithms, data structures (specifically 2D arrays or matrices), and problem-solving strategies. The goal is to calculate the perimeter of a single island in a grid, where the grid is represented as a 2D array of integers.

You are tasked with creating a Python function `def island_perimeter(grid):` that calculates the perimeter of the island defined in the grid.

## Project Details

- **Grid Representation**:
  - `0` represents water.
  - `1` represents land.
  - Each cell is square with a side length of 1.
  - The island cells are connected horizontally or vertically (not diagonally).
  - The grid is completely surrounded by water.
  - There is only one island, and the island has no internal lakes.

### Example:
```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12
```

### Task

- You are required to implement a function `island_perimeter(grid)` that returns the perimeter of the island.
  
### Concepts Needed:

1. **2D Arrays (Matrices)**:  
   Learn how to access and iterate over elements in a 2D array and how to navigate adjacent cells (horizontally and vertically).
  
2. **Conditional Logic**:  
   Apply conditions to determine whether a cell contributes to the perimeter of the island.
  
3. **Counting Techniques**:  
   Develop a strategy to count the edges that contribute to the island's perimeter.
  
4. **Problem-Solving Strategies**:  
   Break the problem into smaller steps, such as identifying land cells and determining how each contributes to the perimeter.

## Requirements

- Files must be executed and interpreted using Python 3.4.3 on Ubuntu 20.04 LTS.
- Files must end with a new line.
- The first line of all Python scripts must be `#!/usr/bin/python3`.
- The PEP 8 style guide (version 1.7) should be adhered to.
- No modules should be imported.
- All functions and modules must be documented.
- All files must be executable.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Rugwiroparfait/0x09-island-perimeter.git
   cd 0x09-island-perimeter
   ```

2. Run the script with sample grid data:
   ```bash
   ./0-main.py
   ```

3. Expected output:
   ```bash
   12
   ```

## Resources

- **Python Official Documentation**: [Nested Lists in Python](https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions)
- **GeeksforGeeks**: [Python Multi-dimensional Arrays](https://www.geeksforgeeks.org/multidimensional-arrays-in-python/)
- **TutorialsPoint**: [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm)

## Author

- [Your Name](https://github.com/Rugwiroparfait)

---

