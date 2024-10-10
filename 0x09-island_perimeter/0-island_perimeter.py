#!/usr/bin/python3
"""
Island Perimeter Module
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.

    Args:
        grid (list of list of ints): 2D array representing the grid where
                                     0 is water and 1 is land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check if the current cell is at the boundary or next to water
                # Check top
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1
                # Check bottom
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1
                # Check left
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1
                # Check right
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1

    return perimeter
