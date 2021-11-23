# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/11/22 9:46
# @Author  : yangwenwen
"""
@Function: 给你一个链表的头节点 head ，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
如果链表中存在环，则返回 true 。 否则，返回 false 。

示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：
输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：
输入：head = [1], pos = -1
输出：false
解释：链表中没有环。

"""

# Definition for singly-linked list.
from leetcode.code.common_func.LinkedList import CircleLink, ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = slow = head
        # 可以这么用的原因在于
        # 若为有环，则可以执行到fast==slow，那么会 return True
        # 若为无环，那可以执行到fast.next为空，会跳出循环 return False
        # 由于fast是跳两次，所以如果直接 while fast.next，会出现空节点.next报错
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


# head = [3,2,0,-4], pos = 1
# head = [1,2], pos = 0
# head = [1], pos = -1
circle_link = CircleLink(node_list=[3, 2, 0, -4], pos=1)
circle_link.setup()
circle_link.show()
print(Solution().hasCycle(circle_link.head))
