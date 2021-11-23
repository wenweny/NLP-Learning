# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/11/16 9:12
# @Author  : yangwenwen
"""
@Function:
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
"""

# Definition for singly-linked list.
from leetcode.code.common_func.LinkedList import ListNode, LinkList


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head_node = ListNode()
        head = head_node
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                print("1:", head.next.val)
                head = head.next
                l1 = l1.next
            else:
                head.next = l2
                print("2:", head.next.val)
                head = head.next
                l2 = l2.next
        if l1:
            head.next = l1
            print("3:", head.next.val)
        elif l2:
            head.next = l2
            print("4:", head.next.val)
        return head_node.next


l1 = [1, 2, 4]
l2 = [1, 3, 4]
l1_link_list = LinkList(l1)
l1_link_list.setup()
l1_link_list.show()

l2_link_list = LinkList(l2)
l2_link_list.setup()
l2_link_list.show()
out_node = Solution().mergeTwoLists(l1_link_list.head, l2_link_list.head)
LinkList([]).show(out_node)
