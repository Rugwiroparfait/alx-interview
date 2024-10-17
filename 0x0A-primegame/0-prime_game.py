#!/usr/bin/python3
"""
Module: 0-prime_game
This module contains the function isWinner, which determines the winner
of the prime number game.
"""


def isWinner(x, nums):
    """
    Determines the winner of x rounds of the game.

    Args:
    x (int): Number of rounds.
    nums (List[int]): List of integers, each/
    representing the range of numbers in a round.

    Returns:
    str: "Maria" if Maria wins more rounds,/
    "Ben" if Ben wins more rounds, None if it's a tie.
    """
    if x < 1 or not nums:
        return None

    # Create a helper function to find all primes /
    # using the Sieve of Eratosthenes
    def sieve(n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return primes

    max_num = max(nums)
    primes = sieve(max_num)

    # Maria wins a round if the number of prime/
    # removals is odd; Ben wins if it's even
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_count = sum(primes[1:n+1])
        if primes_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
