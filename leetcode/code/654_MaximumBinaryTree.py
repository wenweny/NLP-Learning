# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/12/20 9:16
# @Author  : yangwenwen
"""
@Function: 654 最大二叉树

给定一个不含重复元素的整数数组 nums 。一个以此数组直接递归构建的 最大二叉树 定义如下：

二叉树的根是数组 nums 中的最大元素。
左子树是通过数组中 最大值左边部分 递归构造出的最大二叉树。
右子树是通过数组中 最大值右边部分 递归构造出的最大二叉树。
返回有给定数组 nums 构建的 最大二叉树 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
from typing import List
from leetcode.code.common_func.BinaryTree import Tree, TreeNode


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) < 1:
            return
        max_num, max_num_index = self.find_max(nums)
        root = TreeNode(max_num)

        root.left = self.constructMaximumBinaryTree(nums[:max_num_index])
        root.right = self.constructMaximumBinaryTree(nums[max_num_index + 1:])
        return root

    def find_max(self, nums: List[int]):
        # 找到最大值，并把最大值与它所在的索引返回
        max_num = 0
        max_num_index = 0
        for idx, num in enumerate(nums):
            if num > max_num:
                max_num = num
                max_num_index = idx
        return max_num, max_num_index



s = Solution()
root = s.constructMaximumBinaryTree(nums=[3, 2, 1, 6, 0, 5])
Tree().show(root)

