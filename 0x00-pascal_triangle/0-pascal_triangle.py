def pascal_triangle(n):
    """
    Generate Pascal's triangle of n rows.

    Args:
    n (int): Number of rows in Pascal's triangle.

    Returns:
    List[List[int]]: Pascal's triangle represented as a list of lists.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        current_row = [1]

        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])

        current_row.append(1)
        triangle.append(current_row)

    return triangle

