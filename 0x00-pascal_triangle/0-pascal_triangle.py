#!/usr/bin/python3

""" Pascal's Triangle 
        Given a non-negative integer n, generate the first n rows of Pascal's
        triangle.
        Returns an empty list if n <= 0
        Example:
        pascal_triangle(5)
        Returns:
        [
                [1],
                [1, 1],
                [1, 2, 1],
                [1, 3, 3, 1],
                [1, 4, 6, 4, 1]
        ]
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        # Create a new row with all elements initialized to 1
        row = [1] * (i + 1)

        # Each element (except the first and last) is the sum of the two
        # elements above it
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
