'''
How many ways to exchange m dollars by [x, y, z] dollars ? (Shopee interview - Data scientist)

'''



from functools import lru_cache
# from functools import lru_cache

# class Solution:
#     def change(self, amount, coins):
#         @lru_cache(10000000000)
#         def coin_exchange_3(tuple_):
#             money, coin_list = tuple_

#             if money == 0:
#                 return 1
#             if money < 0:
#                 return 0
#             if len(coin_list) <= 0:
#                 return 0
#             return coin_exchange_3((money, coin_list[:-1]) ) + coin_exchange_3((money - coin_list[-1], coin_list))

#         tuple_ = (amount, tuple(coins))
#         return coin_exchange_3(tuple_)

#
# class Solution:
#
#     def change(self, amount, coins):
#         def coin_exchange_2(money, coin_list, mem_cache):
#             key = (money, coin_list)
#             if key in mem_cache:
#                 return mem_cache[key]
#
#             if money == 0:
#                 return 1
#             if money < 0:
#                 return 0
#             if len(coin_list) <= 0:
#                 return 0
#             mem_cache[key] = coin_exchange_2(money, coin_list[:-1], mem_cache) + coin_exchange_2(money - coin_list[-1], coin_list, mem_cache)
#             return mem_cache[key]
#
#         mem = dict()
#         return coin_exchange_2(amount, tuple(coins), mem)
#
# coins = [270, 373, 487, 5, 62]
# amount = 8121
# test= Solution()
# print("test.change(20, [10,20,30])", test.change(amount, coins))
#
#
#

###
"""
    xai key tuple nhanh hon key string (convert list to string())
"""
import math

class Solution:
    def change(self, amount, coins):
        def coin_exchange_helper(amount, mem):
            if amount in mem:
                return mem[amount]
            if amount == 0:
                return 1
            if amount < 0:
                return 0
            res = 0

            for coin in coins:
                temp = coin_exchange_helper(amount - coin, mem)
                if temp != math.inf:
                    res += temp
            mem[amount] = res
            return res


        mem = dict()
        res = coin_exchange_helper(amount, mem)
        if res == math.inf:
            return -1
        else:
            return res



coins = [1, 2, 5]
amount = 5
test= Solution()
print("test.change()", test.change(amount, coins))