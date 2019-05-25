"""
    Created by chaupm at 2019-05-16
"""
import math

from functools import lru_cache


class Solution:
    def coinChange(self, coins, amount):
        @lru_cache(100000)
        def coin_exchange_helper(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return math.inf
            return min(coin_exchange_helper(amount - coin) for coin in coins) + 1

        if len(coins) == 1:
            if amount % coins[0] > 0:
                return -1
            else:
                return amount // coins[0]
        res = coin_exchange_helper(amount)
        return -1 if res == math.inf else res

    def coinChange_bottomUp(self, coins, amount):
        @lru_cache(100000)
        def coin_exchange_helper(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return math.inf
            return min(coin_exchange_helper(amount - coin) for coin in coins) + 1

        if len(coins) == 1:
            if amount % coins[0] > 0:
                return -1
            else:
                return amount // coins[0]
        res = coin_exchange_helper(amount)
        return -1 if res == math.inf else res

coin_list = [1,3, 5] #[270,373,487,5,62]
money = 8  #8121

test = Solution()
print(test.coinChange(coin_list, money))
