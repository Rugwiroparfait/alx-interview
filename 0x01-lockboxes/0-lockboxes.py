#!/usr/bin/python3
"""
This module contains a function to determine if all boxes can be unlocked.

The `canUnlockAll` function uses a breadth-first
search approach to check if all
boxes in a given list can be unlocked starting from the first box.

Author: Your Name
"""

from collections import deque

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked.

    Args:
        boxes (list of list of int): A list of lists where each
        sublist represents
        a box and contains keys to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    queue = deque([0])
    visited = set()

    while queue:
        current_box = queue.popleft()

        if current_box in visited:
            continue

        visited.add(current_box)

        keys = boxes[current_box]
        for key in keys:
            if 0 <= key < len(boxes) and key not in visited:
                queue.append(key)

    return len(visited) == len(boxes)
