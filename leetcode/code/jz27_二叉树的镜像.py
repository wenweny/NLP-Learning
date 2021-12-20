# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/12/20 9:44
# @Author  : yangwenwen
"""
@Function: 请完成一个函数，输入一个二叉树，该函数输出它的镜像。

"""
from leetcode.code.common_func.BinaryTree import Tree, TreeNode


class Solution:
    def mirrorTree_notwell(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root = self.mirror(root)
        root.left = self.mirrorTree(root.left)
        root.right = self.mirrorTree(root.right)
        return root

    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        tmp = root.right
        root.right = self.mirrorTree(root.left)
        root.left = self.mirrorTree(tmp)
        return root

    def mirror(self, root):
        tmp = root.left
        root.left = root.right
        root.right = tmp
        return root


s = Solution()
binary_tree = Tree()
root = binary_tree.setup([1, 1111, 22, 1111, 2, 3, 4, 1, 2, 3, 4, 5, 6, 7, 8])
binary_tree.show(root)
root_mirror = s.mirrorTree(root)
binary_tree.show(root_mirror)
