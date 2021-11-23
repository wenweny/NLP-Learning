> [Leetcode141 简单题](https://leetcode-cn.com/problems/linked-list-cycle/) 环形链表

## 题目描述

给你一个链表的头节点 head ，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

如果链表中存在环，则返回 true 。 否则，返回 false 。

 

**示例 1：**

输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。

**示例 2：**

输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。

**示例 3：**

输入：head = [1], pos = -1
输出：false
解释：链表中没有环。

## 题目解答

```python
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
```

解题关键在于有返回中止条件，所以可以这么使用while

另外，就没人觉得leetcode上只有解题函数，而没有全部函数用于线下测试，而感到苦恼吗？

写了创建环形链表和展示的逻辑，方便本地测试。

```python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

```

