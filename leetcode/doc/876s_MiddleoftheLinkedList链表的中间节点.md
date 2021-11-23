> [leetcode 876简单题](https://leetcode-cn.com/problems/middle-of-the-linked-list/)

## 题目描述

给定一个头结点为 head 的非空单链表，返回链表的中间结点。
如果有两个中间结点，则返回第二个中间结点。

**示例 1：**
输入：[1,2,3,4,5]
输出：此列表中的结点 3 (序列化形式：[3,4,5])
返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
注意，我们返回了一个 ListNode 类型的对象 ans，这样：
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.

**示例 2：**
输入：[1,2,3,4,5,6]
输出：此列表中的结点 4 (序列化形式：[4,5,6])
由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。

## 题目解答

```python
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        # 若题目改为 当中间节点有两个，返回第一个时
        # 条件改为 while fast.next and fast.next.next
        while fast and fast.next:
            print(fast.val)
            slow = slow.next
            fast = fast.next.next
        return slow
```

**全部代码**

```python
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


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        # 若题目改为 当中间节点有两个，返回第一个时
        # 条件改为 while fast.next and fast.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


link_list = LinkList([1, 2, 3, 4, 5, 6])
link_list.setup()
link_list.show()
print(Solution().middleNode(link_list.head).val)
```

**举一反三：**若题目改为 当中间节点有两个，返回第一个时，条件改为 while fast.next and fast.next.next

