Here’s a structured **README.md** for your project based on the task description:

---

# 0x08. Making Change

## Project Overview

This project tackles the **coin change problem**, a classic problem in dynamic programming and greedy algorithms. The objective is to determine the **fewest number of coins** required to make up a given total amount, given a list of coin denominations.

### Key Concepts

1. **Greedy Algorithms**:
   - Understand how greedy algorithms can be used to solve the problem.
   - Recognize the limitations of greedy approaches and when they might fail to provide an optimal solution.

2. **Dynamic Programming**:
   - Use dynamic programming to solve optimization problems.
   - Learn the concepts of **overlapping subproblems** and **optimal substructure** in the coin change problem.

3. **Algorithmic Complexity**:
   - Analyze and optimize time and space complexity.
   - Strive for efficient solutions to meet runtime constraints.

4. **Problem-Solving Strategies**:
   - Break down the problem into manageable sub-problems.
   - Explore iterative vs. recursive approaches in dynamic programming.

### Python Skills
- Manipulate lists and use list comprehensions.
- Implement functions using loops and conditional statements.

---

## Task: Change Comes from Within

### Problem Description

Given a pile of coins of different values, determine the **fewest number of coins** needed to meet a given total amount.

### Function Prototype
```python
def makeChange(coins, total):
```

### Function Requirements

- **Input**: 
  - `coins`: A list of integers representing coin denominations.
  - `total`: The target amount to reach.
  
- **Output**:
  - Return the fewest number of coins needed to meet the `total`.
  - If the `total` is 0 or less, return `0`.
  - If the `total` cannot be met by any combination of coins, return `-1`.

### Example
```python
makeChange([1, 2, 25], 37)  # Output: 7
makeChange([1256, 54, 48, 16, 102], 1453)  # Output: -1
```

---

## Requirements

- Your files should follow the **PEP 8** style guide (version 1.7.x).
- Code will be interpreted/compiled on **Ubuntu 20.04 LTS** using Python3 (version 3.4.3).
- All your files must be executable.
- Ensure your solution’s runtime efficiency is optimal.

---

## Resources

- **Python Documentation**: Learn more about control flow tools such as `for` loops and `if` statements.
- **GeeksforGeeks**:
  - [Coin Change Problem (DP-7)](https://www.geeksforgeeks.org/coin-change-dp-7/)
  - [Greedy Algorithm for Minimum Number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)
- **YouTube**: 
  - [Dynamic Programming - Coin Change Problem](https://www.youtube.com/watch?v=Y0ZqKpToTic)

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/alx-interview.git
   ```
   
2. Navigate to the project directory:
   ```bash
   cd 0x08-making_change
   ```

3. Run the test file:
   ```bash
   ./0-main.py
   ```

---

## Author
Project developed as part of the **ALX Specialization Program**.

---
