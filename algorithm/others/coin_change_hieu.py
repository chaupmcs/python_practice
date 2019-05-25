"""
    Created by chaupm at 2019-05-17
"""

import math
class Solution:
    def coinChange(self, coins, amount):
        def countStep(subAmount, map):
            min_of_list = math.inf
            for coin in coins:
                if (subAmount - coin) in map:
                    min_of_list = min(map[(subAmount - coin)], min_of_list)
                    map[subAmount] = min_of_list + 1

        if amount == 0:
            return 0

        map = {}
        for coin in coins:
            map[coin] = 1

        for i in range(1, amount + 1):
            if i not in coins:
                countStep(i, map)

        return map.get(amount, -1)


def a(map_, list_ = None):
    if list_ is not None:
        list_.append("haha")
    map_["xx"] = 100

map___ = {10:10000}
list___ = ["aa"]


a(map___, list___)
a(map___, list___)

print(map___)
print(list___)

coins = [1,2,5]
amount = 11

test = Solution()
print(test.coinChange(coins, amount))