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

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkList:
    def __init__(self, node_list: List):
        self.list = node_list
        self.head = ListNode()

    def setup(self):
        cur = self.head
        for value in self.list:
            node = ListNode(value)
            cur.next = node
            cur = cur.next

    def show(self, cur=None):
        output_val: List[str] = []
        if not cur:
            cur = self.head.next
        while cur:
            output_val.append(str(cur.val))
            cur = cur.next
        print("->".join(output_val))


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head_node = ListNode()
        head = head_node
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                print("1:",head.next.val)
                head = head.next
                l1 = l1.next
            else:
                head.next = l2
                print("2:",head.next.val)
                head = head.next
                l2 = l2.next
        if l1:
            head.next = l1
            print("3:",head.next.val)
        elif l2:
            head.next = l2
            print("4:",head.next.val)
        return head_node.next


l1 = [1, 2, 4]
l2 = [1, 3, 4]
l1_link_list = LinkList(l1)
l1_link_list.setup()
l1_link_list.show()

l2_link_list = LinkList(l2)
l2_link_list.setup()
l2_link_list.show()
out_node = Solution().mergeTwoLists(l1_link_list.head.next, l2_link_list.head.next)
LinkList([]).show(out_node)
