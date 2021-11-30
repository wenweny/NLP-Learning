# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/11/30 9:45
# @Author  : yangwenwen
"""
@Function: 
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

示例 2：
输入：head = [1], n = 1
输出：[]

示例 3：
输入：head = [1,2], n = 1
输出：[1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from leetcode.code.common_func.LinkedList import ListNode, LinkList


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        # 需要虚拟头结点的技巧，是为了防止出现空指针的情况，
        # 比如说链表总共有5个节点，题目就让你删除倒数第5个节点，也就是第一个节点，
        # 那按照算法逻辑，应该首先找到倒数第6个节点。
        # 但第一个节点前面已经没有节点了，这就会出错。
        # 但有了我们虚拟节点dummy的存在，就避免了这个问题，能够对这种情况进行正确的删除。
        dummy = ListNode()
        dummy.next = head

        fast = slow = dummy

        for i in range(n):
            fast = fast.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next
            
        # 否则在这会出错，NoneType没有.next
        slow.next = slow.next.next
        return dummy.next


s = Solution()

l1 = LinkList([1, 2, 3, 4, 5])
# l1 = LinkList([1])
l1.setup()
l1.show()

result_node = s.removeNthFromEnd(head=l1.head, n=2)
# result_node = s.removeNthFromEnd(head=l1.head, n=1)

LinkList([]).show(cur=result_node)  # [1,2,3,5]
