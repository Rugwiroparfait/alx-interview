# 0x07. Rotate 2D Matrix

## Description
In this project, you are required to implement an in-place algorithm that rotates an `n x n` 2D matrix by 90 degrees clockwise. The goal is to achieve the rotation without using extra memory, meaning that you need to manipulate the matrix directly rather than creating a copy.

This project helps in understanding matrix manipulation, in-place operations, and space complexity optimization.

## Key Concepts

### 1. Matrix Representation in Python
- Matrices in Python are represented using lists of lists. Each inner list corresponds to a row in the matrix.
- You should know how to access and modify elements in this structure.

### 2. In-place Operations
- In-place operations modify data directly without creating a new copy, which reduces space complexity.
- This task requires modifying the input matrix directly.

### 3. Matrix Transposition
- The process of swapping rows and columns in a matrix. This is the first step in the rotation process.

### 4. Reversing Rows
- After transposing the matrix, each row must be reversed to achieve a 90-degree clockwise rotation.

### 5. Nested Loops
- Nested loops are used to traverse and modify the 2D matrix.
  
## Requirements

- You are **not allowed to import any module**.
- The code should be written in Python 3 and be compatible with Ubuntu 20.04 LTS.
- All your code should follow **pycodestyle** guidelines.
- All files should be executable.
- All modules and functions must be documented.

## Task

### Rotate 2D Matrix
- **Objective**: Rotate the given `n x n` matrix by 90 degrees clockwise.
- **Prototype**: 
    ```python
    def rotate_2d_matrix(matrix):
    ```
- **Input**: An `n x n` matrix where `n` is the number of rows and columns.
- **Output**: The matrix should be modified **in-place**. No return value is expected.

### Example:
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_2d_matrix(matrix)

print(matrix)
```
**Output**:
```
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

## Approach

To rotate the matrix:
1. **Transpose the matrix** (swap rows and columns).
2. **Reverse each row** to complete the 90-degree clockwise rotation.

## Resources

### Official Python Documentation
- [Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

### Additional References:
- [GeeksforGeeks: Inplace Rotate Square Matrix by 90 Degrees](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
- [GeeksforGeeks: Transpose a Matrix in Python](https://www.geeksforgeeks.org/python-transpose-matrix/)

## Mock Technical Interview
For further practice, consider preparing for technical interviews using the same concepts covered in this project.

## Files

- **`0-rotate_2d_matrix.py`**: Your implementation of the rotation algorithm.
- **`main_0.py`**: The test file to validate your function.

### Testing Example:
```bash
jessevhedden$ cat main_0.py
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
```
**Expected Output**:
```bash
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

## Repository
- **GitHub Repository**: `alx-interview`
- **Directory**: `0x07-rotate_2d_matrix`
- **File**: `0-rotate_2d_matrix.py`

---
