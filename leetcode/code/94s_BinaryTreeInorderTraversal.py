# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/12/6 9:42
# @Author  : yangwenwen
"""
@Function: 
给定一个二叉树的根节点 root ，返回它的 中序 遍历。
"""
from leetcode.code.common_func.BinaryTree import TreeNode, Tree
from typing import List

input_list = [1, None, 2, None, None, 3, None]
tree = Tree()
tree_root = tree.setup(val_list=input_list)


class Solution:
    """中序遍历"""

    # 递归
    def inorderTraversal_recursion(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if not root:
            return None

        self.dfs(root.left, res)
        res.append(root.val)
        self.dfs(root.right, res)

        return res

    # 迭代
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                root = tmp.right

        return res


in_order_list = Solution().inorderTraversal(tree_root)
print(in_order_list)
