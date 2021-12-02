# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/12/2 9:55
# @Author  : yangwenwen
"""
@Function: 二叉树的通用操作

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None

    # 前序遍历 根节点-左节点-右节点
    def pre_order_traversal(self, root):
        val_list = []
        if root:
            val_list.append(root.val)
            self.pre_order_traversal(root.left)
            self.pre_order_traversal(root.right)
        return val_list

    # 根据层次遍历得到的列表创建二叉树，空节点用none表示
    def setup(self, val_list):
        def level(index):
            if index >= len(val_list) or val_list[index] is None:
                return None
            root = TreeNode(val_list[index])
            root.left = level(2 * index + 1)
            root.right = level(2 * index + 2)

            return root

        self.root = level(0)
        return level(0)

    def get_depth(self, root):
        if not root:
            return 0
        else:
            return max(self.get_depth(root.left), self.get_depth(root.right)) + 1

    # def write_array(self, current_node, row, col, res, depth):
    #     if not current_node:
    #         return
    #     print(current_node.val)
    #     res[row][col] = str(current_node.val)
    #     current_level = (row + 1) // 2
    #     if current_level == depth:
    #         return
    #     gap = depth - current_level - 1
    #
    #     if current_node.left:
    #         res[row + 1][col - gap] = "/"
    #         self.write_array(current_node.left, row + 2, col - gap * 2, res, depth)
    #     if current_node.right:
    #         res[row + 1][col + gap] = "\\"
    #         self.write_array(current_node.right, row + 2, col + gap * 2, res, depth)
    #
    # def show(self, root):
    #     if not root:
    #         print("empty")
    #
    #     depth = self.get_depth(root)
    #     height = depth * 2 - 1
    #     width = pow(2, (depth - 2) * 3 + 1)
    #
    #     res = [[" " for i in range(width)] for j in range(height)]
    #     self.write_array(root, 0, int(width / 2), res, depth)
    #
    #     # 打印输出
    #     for i in range(height):
    #         print("".join(res[i]))

    def write_array(self, current_node, row, col, res, depth):
        deepest_gap = 3
        if not current_node:
            return
        # print(current_node.val)
        # gap = col // 2
        print("row:", row, "col:", col, "val:", current_node.val)
        res[row][col] = str(current_node.val)

        current_level = row
        if current_level == depth:
            return

        if current_node.left:
            # res[row + 1][col - gap] = "/"
            self.write_array(current_node.left, row + 1, col - deepest_gap-1, res, depth)
        if current_node.right:
            # res[row + 1][col + gap] = "\\"
            self.write_array(current_node.right, row + 1, col + deepest_gap, res, depth)

    def show(self, root):
        if not root:
            print("empty")

        depth = self.get_depth(root)
        height = depth
        deepest_num = pow(2, depth - 1)
        deepest_gap = 3
        width = (deepest_num - 1) * deepest_gap + deepest_num

        res = [["*" for i in range(width)] for j in range(height)]
        self.write_array(root, 0, width // 2, res, depth)
        print(res)

        # 打印输出
        for i in range(height):
            print("".join(res[i]))


if __name__ == "__main__":
    binary_tree = Tree()
    root = binary_tree.setup([1, 1, 2, 1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 7, 8])
    # binary_tree.show(root)
    height = binary_tree.get_depth(binary_tree.root)
    print("height:", height)
    binary_tree.show(binary_tree.root)
