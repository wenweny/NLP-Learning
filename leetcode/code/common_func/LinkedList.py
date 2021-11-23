# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/11/23 9:55
# @Author  : yangwenwen
"""
@Function: 链表共用函数
"""
from typing import List


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
        self.head = self.head.next

    def show(self, cur=None):
        output_val: List[str] = []
        if not cur:
            cur = self.head
        while cur:
            output_val.append(str(cur.val))
            cur = cur.next
        print("->".join(output_val))


class CircleLink:
    def __init__(self, node_list, pos=-1):
        self.list = node_list
        self.head = ListNode()
        self.pos = pos
        self.show_value = []

    def setup(self):
        cur = self.head
        tmp = ListNode()
        for idx, value in enumerate(self.list):
            # 创建一个节点
            node = ListNode(value)
            if idx == self.pos:
                tmp = node
            cur.next = node
            self.show_value.append((idx, node.val))
            cur = cur.next
        cur.next = tmp
        self.show_value.append((self.pos, tmp.val))

    def show(self):
        output_list = []
        for (idx, val) in self.show_value:
            output_list.append("idx:" + str(idx) + ",val:" + str(val) + " ")
        print("->".join(output_list))