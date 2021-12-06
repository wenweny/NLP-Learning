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
        self.deepest_gap = 7

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

    def write_array2(self, current_node, row, col, res, depth):
        if not current_node:
            return

        res[row][col] = str(current_node.val)
        current_level = (row + 1) // 2
        if current_level == depth:
            return
        gap = depth - current_level - 1
        # gap=int(((self.deepest_gap + 1) // 2) * pow(2, (depth - row - 2)))
        # print("row:", row, "col:", col, "val:", current_node.val, "level:", current_level, "gap:", gap)

        if current_node.left:
            res[row + 1][col - gap] = "/"
            self.write_array2(current_node.left, row + 2, col - gap * 2, res, depth)
        if current_node.right:
            res[row + 1][col + gap] = "\\"
            self.write_array2(current_node.right, row + 2, col + gap * 2, res, depth)

    def show2(self, root):
        if not root:
            print("empty")

        depth = self.get_depth(root)
        height = depth * 2 - 1
        # width = pow(2, (depth - 2) * 3 + 1)
        deepest_num = pow(2, depth - 1)
        width = (deepest_num - 1) * self.deepest_gap + deepest_num

        res = [[" " for i in range(width)] for j in range(height)]
        self.write_array2(root, 0, int(width / 2), res, depth)

        # 打印输出
        # for i in range(height):
        #     print("".join(res[i]))
        self.format_output(res)

    def write_array(self, current_node, row, col, res, depth):
        if not current_node or row == depth:
            return

        res[row][col] = str(current_node.val)

        # 最末尾节点的间隔 往上只是一直*2
        gap = ((self.deepest_gap + 1) // 2) * pow(2, (depth - row - 2))
        if current_node.left:
            # res[row + 1][col - gap] = "/"
            self.write_array(current_node.left, row + 1, col - gap, res, depth)
        if current_node.right:
            # res[row + 1][col + gap] = "\\"
            self.write_array(current_node.right, row + 1, col + gap, res, depth)

    def show(self, root):
        if not root:
            print("empty")

        depth = self.get_depth(root)
        deepest_num = pow(2, depth - 1)
        # 叶子节点个数+两两节点中间之和
        width = (deepest_num - 1) * self.deepest_gap + deepest_num

        res = [[" " for i in range(width)] for j in range(depth)]
        self.write_array(root, 0, width // 2, res, depth)
        self.format_output(res)

    def format_output(self, out_list):
        # 打印输出
        format_out = ""
        height, width = len(out_list), len(out_list[0])
        for i in range(height):
            format_out += "\n"
            j = 0
            while j < width:
                now_val = str(out_list[i][j])
                format_out += now_val
                # 若当前数字大于一个字符，则跳过n个空格输出，使后面的字符保持格式
                if len(now_val) > 1:
                    j += len(now_val)
                else:
                    j += 1
        print(format_out)


if __name__ == "__main__":
    binary_tree = Tree()
    root = binary_tree.setup([1, 1111, 22, 1111, 2, 3, 4, 1, 2, 3, 4, 5, 6, 7, 8])
    # binary_tree.show(root)
    height = binary_tree.get_depth(binary_tree.root)
    print("height:", height)
    binary_tree.show(binary_tree.root)
    binary_tree.show2(binary_tree.root)

    # res = [["*" for i in range(29)] for j in range(4)]
    # res[0][14] = '1'
    # res[1][14 - 8] = '1'
    # res[1][14 + 8] = '2'
    # res[2][6 - 4] = '1'
    # res[2][6 + 4] = '2'
    # res[2][22 - 4] = '3'
    # res[2][22 + 4] = '4'
    # res[3][2 - 2] = '1'
    # res[3][2 + 2] = '2'
    # res[3][10 - 2] = '3'
    # res[3][10 + 2] = '4'
    # res[3][18 + 2] = '5'
    # res[3][18 - 2] = '6'
    # res[3][26 - 2] = '7'
    # res[3][26 + 2] = '8'
    # # 打印输出
    # for i in range(4):
    #     print("".join(res[i]))
