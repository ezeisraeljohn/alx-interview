#!/usr/bin/python3


def island_perimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4

                # Check if the cell above is also land
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2

                # Check if the cell to the left is also land
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2
