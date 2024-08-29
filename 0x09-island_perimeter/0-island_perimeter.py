#!/usr/bin/python3

""" The Island Perimeter Problem """


def island_perimeter(grid):
    """The function that calculates the perimeter of the island"""
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4

                # Check if the cell above is also land
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2  # Shared border with the cell above

                # Check if the cell to the left is also land
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2  # Shared border with the cell on the left

    return perimeter
