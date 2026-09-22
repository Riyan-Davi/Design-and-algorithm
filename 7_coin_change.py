"""
Program 7: Implementation of Making a Change (Coin Change) Problem
Using Dynamic Programming
"""

import time


def coin_change_min_coins(coins, amount):
    """
    Returns the minimum number of coins needed to make up 'amount',
    and the coins used. Returns (-1, []) if it's not possible.
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)

    for a in range(1, amount + 1):
        for c in coins:
            if c <= a and dp[a - c] + 1 < dp[a]:
                dp[a] = dp[a - c] + 1
                coin_used[a] = c

    if dp[amount] == float('inf'):
        return -1, []

    # Reconstruct the coins used
    result = []
    a = amount
    while a > 0:
        c = coin_used[a]
        result.append(c)
        a -= c

    return dp[amount], result


def coin_change_count_ways(coins, amount):
    """
    Returns the total number of distinct ways to make up 'amount'
    using the given coins (order doesn't matter, unlimited supply).
    """
    dp = [0] * (amount + 1)
    dp[0] = 1

    for c in coins:
        for a in range(c, amount + 1):
            dp[a] += dp[a - c]

    return dp[amount]


def main():
    coins = [1, 2, 5, 10]
    amount = 27

    print("Available coins:", coins)
    print("Target amount:", amount)

    start = time.perf_counter()
    min_coins, coins_used = coin_change_min_coins(coins, amount)
    end = time.perf_counter()

    if min_coins == -1:
        print(f"\nIt is not possible to make {amount} with the given coins.")
    else:
        print(f"\nMinimum number of coins needed: {min_coins}")
        print("Coins used:", coins_used)
    print(f"Time taken: {end - start:.6f} sec")

    ways = coin_change_count_ways(coins, amount)
    print(f"\nTotal number of ways to make {amount}: {ways}")


if __name__ == "__main__":
    main()