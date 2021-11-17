from typing import List


class Solution:
    def two_sum_bad(self, nums: List[int], target: int) -> List[int]:
        left_idx = 0
        right_idx = len(nums) - 1
        while left_idx < len(nums) - 1:
            while right_idx > left_idx:
                if nums[left_idx] + nums[right_idx] == target:
                    return [left_idx, right_idx]
                else:
                    right_idx -= 1
            left_idx += 1
            right_idx = len(nums) - 1

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_dict = dict()
        for idx, num in enumerate(nums):
            other_num = target - num
            if other_num in hash_dict:
                # hash_dict[other_num] 就是上一次存在hash_dict[num]的数字
                return [hash_dict[other_num],idx]
            else:
                hash_dict[num] = idx


nums = [2, 3, 4]
target = 7
print(Solution().twoSum(nums, target))
