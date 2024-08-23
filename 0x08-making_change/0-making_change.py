#!/usr/bin/python3

""" This carries out the making change problem """


from collections import deque


def makeChange(coins, total):
    """This function calculates the minimum number of coins needed to make a
    total

    Args:
        coins: list of integers
        total: integer

        Returns:
            integer: minimum number of coins needed to make the total

            Example:
                coins = [1, 2, 5]
                total = 11
                makeChange(coins, total) -> 3
    """

    if total <= 0:
        return 0

    # Initialize the queue for BFS
    queue = deque([(0, 0)])  # (current_amount, num_coins)
    visited = set()  # To avoid re-processing the same amount
    visited.add(0)

    while queue:
        current_amount, num_coins = queue.popleft()

        for coin in coins:
            next_amount = current_amount + coin

            if next_amount == total:
                return num_coins + 1

            if next_amount < total and next_amount not in visited:
                visited.add(next_amount)
                queue.append((next_amount, num_coins + 1))

    return -1
