# 两数之和Two Sum

> 简单题 leetcode1



难度简单12495收藏分享切换为英文接收动态反馈

给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出 **和为目标值** *`target`* 的那 **两个** 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

 

**示例 1：**

```
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
```

**示例 2：**

```
输入：nums = [3,2,4], target = 6
输出：[1,2]
```

**示例 3：**

```
输入：nums = [3,3], target = 6
输出：[0,1]
```

 

**提示：**

- `2 <= nums.length <= 104`
- `-109 <= nums[i] <= 109`
- `-109 <= target <= 109`
- **只会存在一个有效答案**

**进阶：**你可以想出一个时间复杂度小于 `O(n2)` 的算法吗？

## 解答

**初始思路：**

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left_idx = 0
        right_idx = len(nums) - 1
        while left_idx < (len(nums) - 1) // 2:
            while right_idx > left_idx:
                if nums[left_idx] + nums[right_idx] == target:
                    return [left_idx, right_idx]
                else:
                    right_idx -= 1
            left_idx += 1
```

**问题：**

第5行只算前面一半，对于答案都在后半段是不行的，同理right_idx应该每次都要重置为最右一个，否则答案都在后面是不行的。

修改为以下状态，测试通过。

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left_idx = 0
        right_idx = len(nums) - 1
        while left_idx < len(nums) -1:
            while right_idx > left_idx:
                if nums[left_idx] + nums[right_idx] == target:
                    return [left_idx, right_idx]
                else:
                    right_idx -= 1
            left_idx += 1
            right_idx = len(nums) - 1
```

此解题相当于暴力遍历

时间复杂度：$O(N^2)$，最坏情况下数组中任意两个数都要被匹配一次。

空间复杂度：$O(1)$

## 优选答案

使用**哈希表**存储已算过的匹配，这样每个元素只会被算一次。时间复杂度和空间复杂度都为$O(N)$

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_dict = dict()
        for idx, num in enumerate(nums):
            other_num = target - num
            if other_num in hash_dict:
                # hash_dict[other_num] 就是上一次存在hash_dict[num]的数字
                return [hash_dict[other_num],idx]
            else:
                hash_dict[num] = idx
```



