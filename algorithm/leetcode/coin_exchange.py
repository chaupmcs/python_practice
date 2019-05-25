"""
    Created by chaupm at 2019-05-13
"""
from functools import lru_cache

@lru_cache()
def coin_exchange_top_down(coins, amount):
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if len(coins) <= 0:
        return 0
    return coin_exchange_top_down(coins[:-1], amount) + coin_exchange_top_down(coins, amount - coins[-1])


print(coin_exchange_top_down([10, 20, 50, 100], 100))
print(coin_exchange_top_down([10, 20, 50, 100], 50))