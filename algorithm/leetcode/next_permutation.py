"""
https://leetcode.com/problems/next-permutation/
"""
from collections import OrderedDict
# import operator
class Solution(object):
    def nextPermutation(self, nums):
        nums_revered = list(reversed(nums))
        my_dict = OrderedDict()
        for i, (n_1, n_2) in enumerate(zip(nums_revered[:-1], nums_revered[1:])):
            if n_1 not in my_dict:
                my_dict[n_1] = -(i+1)
            if n_1 > n_2:
                left_swap_index = -(i+2)
                # my_dict = sorted(my_dict.items(), key = lambda x: x[1], reverse=True)
                # my_dict = sorted(my_dict.items(), key=operator.itemgetter(1), reverse=True)
                for k, v in my_dict.items():
                    if k > n_2:
                        right_swap_index = v
                        # right_sided_arr = list(reversed(nums[left_swap_index+1:]))
                        # left_sided_arr[-1], right_sided_arr[right_swap_index] = right_sided_arr[right_swap_index], left_sided_arr[-1]

                        nums[left_swap_index], nums[right_swap_index] = nums[right_swap_index], nums[left_swap_index]
                        nums[left_swap_index+1:] = nums[left_swap_index+1:][::-1]
                        return
        nums.reverse()

    def nextPermutation_2(self, nums):
        my_dict = OrderedDict()
        for i in range(len(nums)-1):
            n_t, n_t_minus_1 = nums[-(i+1)], nums[-(i+2)]
            if n_t not in my_dict:
                my_dict[n_t] = -(i+1)
            if n_t > n_t_minus_1:
                left_swap_index = -(i+2)
                for k, v in my_dict.items():
                    if k > n_t_minus_1:
                        right_swap_index = v
                        nums[left_swap_index], nums[right_swap_index] = nums[right_swap_index], nums[left_swap_index]
                        for index in range(left_swap_index+1,(len(nums)-left_swap_index-1)//2):
                            nums[index], nums[len(nums)-index+left_swap_index] = nums[len(nums)-index+left_swap_index], nums[index]
                        return
        nums.reverse()


arr = [5,1,6,5,2,3,2]

# arr_3 = [5,1,4,6,5,3,2] => [5,1,4] + [6,5,3,2] => [5,1,4] + [2,3,5,6] [5,1,5,6,4,3,2]
# arr_4 = [5,1,4,6,5,5, 3,2] => [5,1,4] + [6,5,5,3,2] => [5,1,4] + [2,3,5,5,6] [5,1,5,6,4,3,2]
arr_3 = [5,1,4,6,5,3,2]
arr_4 = [5, 1, 4, 6, 5, 5, 3, 2]
arr_2 = [1,3,2]
arr_5 =[16,27,25,23,25,16,12,9,1,2,7,20,19,23,0,6,22,16,11,8,27,9,2,20,2,13,7,25,29,12,12,18,29,27,13,16,1,22,9,3,21,29,14,7,8,14,5,0,23,16,1,20,16]
arr_6 = [6,7,6,5,4,3,2]
test = Solution()
num_arr = arr_5
test.nextPermutation_2(num_arr)
print(num_arr)