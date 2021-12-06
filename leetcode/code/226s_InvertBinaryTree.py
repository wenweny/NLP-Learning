# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/12/6 9:09
# @Author  : yangwenwen
"""
@Function: 
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

"""

from leetcode.code.common_func.BinaryTree import Tree, TreeNode

input_list = [4, 2, 7, 1, 3, 6, 9]
binary_tree = Tree()
tree_root = binary_tree.setup(val_list=input_list)
binary_tree.show(tree_root)


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        tmp = root.left
        root.left = root.right
        root.right = tmp

        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        return root


invert_root = Solution().invertTree(tree_root)
binary_tree.show(root=invert_root)
