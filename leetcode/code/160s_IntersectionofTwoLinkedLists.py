# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/11/24 9:22
# @Author  : yangwenwen
"""
@Function:
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。
如果两个链表不存在相交节点，返回 null 。

题目数据 保证 整个链式结构中不存在环。
注意，函数返回结果后，链表必须 保持其原始结构 。

输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'
解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,6,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

"""

from leetcode.code.common_func.LinkedList import LinkList


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class IntersectionTwoLink:
    def setup(self, intersectVal, listA, listB, skipA, skipB):
        link_A = LinkList(listA)
        link_A.setup()
        link_A.show()  # 4->1->8->4->5
        link_B = LinkList(listB)
        link_B.setup()
        link_B.show()  # 5->6->1->8->4->5

        cur_A = link_A.head
        cur_B = link_B.head
        for idx in range(skipA):
            cur_A = cur_A.next
        for idx_B in range(skipB):
            cur_B = cur_B.next
        LinkList([]).show(cur_A)  # 8->4->5
        LinkList([]).show(cur_B)  # 8->4->5
        print(cur_A)  # 虽然此时cur_A和cur_B打印出来是一样的
        print(cur_B)  # 但本身cur_A和cur_B是两个不同的对象
        if cur_A and cur_B and cur_A.val == intersectVal:
            print("Intersected at '%s'" % (str(intersectVal)))
        else:
            print("null")
        return link_A.head, link_B.head


headA, headB = IntersectionTwoLink().setup(intersectVal=8,
                                           listA=[4, 1, 8, 4, 5], listB=[5, 6, 1, 8, 4, 5],
                                           skipA=2, skipB=3)


# IntersectionTwoLink().setup(intersectVal=2,
#                             listA=[1, 9, 1, 2, 4], listB=[3, 2, 4],
#                             skipA=3, skipB=1)
# IntersectionTwoLink().setup(intersectVal=0,
#                             listA=[2, 6, 4], listB=[1, 5],
#                             skipA=3, skipB=2)


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        如果用两个指针p1和p2分别在两条链表上前进，并不能同时走到公共节点，也就无法得到相交节点c1。
        所以，解决这个问题的关键是，通过某些方式，让p1和p2能够同时到达相交节点c1
        所以，我们可以让p1遍历完链表A之后开始遍历链表B，让p2遍历完链表B之后开始遍历链表A，
        这样相当于「逻辑上」两条链表接在了一起。
        如果这样进行拼接，就可以让p1和p2同时进入公共部分，也就是同时到达相交节点
        https://labuladong.gitee.io/algo/2/17/16/
        """
        p1 = headA
        p2 = headB
        while p1 != p2:
            # p1走一步，如果走到A链表末尾，转到B链表
            if p1:
                p1 = p1.next
            else:
                p1 = headB
            if p2:
                p2 = p2.next
            else:
                p2 = headA
        return p1


Solution().getIntersectionNode(headA, headB)
