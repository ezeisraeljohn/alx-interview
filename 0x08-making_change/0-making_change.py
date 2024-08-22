#!/usr/bin/python3

""" This carries out the making change problem """


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
    if total < 0:
        return 0
    if total == 0:
        return 0

    dp = [float("inf")] * (total + 1)
    dp[0] = 0  # 0 coins needed to make amount 0

    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] != float("inf"):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float("inf") else -1
