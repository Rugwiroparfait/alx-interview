def canUnlockAll(boxes):
    from collections import deque

    # Initialize the queue with the first box (index 0)
    queue = deque([0])
    visited = set()

    while queue:
        # Get the current box index from the queue
        current_box = queue.popleft()

        # Skip this box if it has already been visited
        if current_box in visited:
            continue

        # Mark the current box as visited
        visited.add(current_box)

        # Get the list of keys in the current box
        keys = boxes[current_box]

        # For each key in the current box
        for key in keys:
            # If the key is within bounds and opens a box that hasn't been visited, add it to the queue
            if 0 <= key < len(boxes) and key not in visited:
                queue.append(key)

    # Check if we've visited all the boxes
    return len(visited) == len(boxes)

