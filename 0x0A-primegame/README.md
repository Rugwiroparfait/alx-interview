---

# 0x0A. Prime Game

## Project Overview

This project focuses on solving a competitive game problem involving prime numbers, game theory, and algorithm optimization. Maria and Ben are playing a game where they take turns removing prime numbers and their multiples from a set of consecutive integers. The objective is to determine the winner based on the given rounds and numbers.

### Key Concepts:
- **Prime Numbers**: Efficient algorithms for identifying prime numbers within a range.
- **Sieve of Eratosthenes**: Used for finding all prime numbers up to a given limit.
- **Game Theory**: Understanding optimal strategies and win conditions for competitive games.
- **Dynamic Programming**: Using memoization to optimize the game logic.

---

## Requirements

- **Editor**: Allowed editors are `vi`, `vim`, `emacs`.
- **Environment**: 
  - Ubuntu 20.04 LTS
  - Python 3.4.3
- **Code Style**: Follow PEP 8 style guide (version 1.7.x).
- **Executable Files**: Ensure all files are executable and end with a new line.
- **README**: A `README.md` file is mandatory at the root of the project folder.

---

## Game Rules

1. Maria and Ben take turns choosing prime numbers from the set of integers from 1 to `n`.
2. Once a prime number is chosen, it and its multiples are removed from the set.
3. The player who cannot make a move loses the game.
4. Maria always goes first, and both players play optimally.

### Task Objective:

Implement the function:
```python
def isWinner(x, nums):
    """
    Determines the winner of each game round.

    Args:
    x (int): Number of rounds.
    nums (List[int]): List of integers representing the end of the range for each round.

    Returns:
    str: Name of the player with the most wins ("Maria" or "Ben").
    """
```

### Example:
```python
x = 3
nums = [4, 5, 1]
```

- **Round 1**: Maria picks 2, Ben picks 3. Ben wins.
- **Round 2**: Maria picks 2, Ben picks 3, Maria picks 5. Maria wins.
- **Round 3**: Ben wins as there are no prime numbers left for Maria to choose.

Result: **Ben wins the game**.

---

## Usage

To run the game and determine the winner:
```bash
./main_0.py
```

Example output:
```
Winner: Ben
```

---

## Algorithm Breakdown

### Sieve of Eratosthenes:
Efficiently find all prime numbers up to a given limit, which helps in determining which primes can be picked during the game.

### Game Logic:
- Track the set of available numbers.
- Players take turns selecting primes and removing their multiples.
- If a player cannot make a move, the other player wins.

### Optimizations:
- **Dynamic Programming**: Store intermediate results to optimize for multiple rounds.
  
---

## Resources

- **Prime Numbers**:
  - [Prime Numbers Introduction](https://www.khanacademy.org)
  - [Sieve of Eratosthenes in Python](https://realpython.com)
  
- **Game Theory Basics**:
  - [Introduction to Game Theory](https://mathsisfun.com)

- **Dynamic Programming**:
  - [Dynamic Programming with Python](https://python-course.eu)

---

## Project Structure

- `0-prime_game.py`: Contains the logic for the prime game.
- `main_0.py`: Sample script to test the game logic.
- `README.md`: Project documentation (this file).

---

## License

This project is licensed under the terms of the MIT License.

---

## Author

- Rugwiro Parfait

---

