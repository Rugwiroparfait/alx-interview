#!/usr/bin/python3
"""
Module to solve the minimum coins needed to make a total amount.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet the total amount.
    Args:
    coins (list): List of coin denominations.
    total (int): The target amount.

    Returns:
    int: The fewest number of coins needed to make the total, or -1 if it's
         not possible.
    """
    if total <= 0:
        return 0

    # Initialize dp array with a large number (infinity)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Build the dp array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
