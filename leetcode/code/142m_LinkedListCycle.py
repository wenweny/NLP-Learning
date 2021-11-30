# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/11/25 9:34
# @Author  : yangwenwen
"""
@Function: 
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
不允许修改 链表。

示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：
输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：
输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode.code.common_func.LinkedList import CircleLink, ListNode,LinkList

p1 = CircleLink(node_list=[3, 2, 0, 4], pos=1)
p1.setup()
p1.show()


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # 相遇证明有环
            if fast == slow:
                break
        # 走完未相遇，且此时fast指向空，判断为无环
        if (not fast) or (not fast.next):
            return None

        # 有环，使slow从头开始，共同走过k-m即是
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return fast


p = Solution()
p_result = p.detectCycle(p1.head)
print(p_result.val)


