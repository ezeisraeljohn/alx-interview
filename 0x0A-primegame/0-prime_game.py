#!/usr/bin/python3

""" This is a solution to the Prime Game problem on HackerRank """


def isWinner(x, nums):
    """Determines the winner of the game based on the number of prime
    selectionsmade by each player."""
    if x < 1 or not nums:
        return None

    # Find the maximum n in nums
    max_n = max(nums)

    # Sieve of Eratosthenes to find all primes up to max_n
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(max_n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False

    # Precompute the number of prime selections for each n
    prime_count = [0] * (max_n + 1)
    for i in range(2, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if sieve[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # Simulate each round
    for n in nums:
        # If the number of prime selections (prime_count[n]) is odd, Maria wins
        # If it's even, Ben wins
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
