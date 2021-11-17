

## 题目描述

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

```txt
示例 1：

输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：

输入：l1 = [], l2 = []
输出：[]
示例 3：

输入：l1 = [], l2 = [0]
输出：[0]
```

## 解题

```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head_node = ListNode()
        head = head_node
        while l1.next and l2.next:
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
        if l1.next:
            head.next = l1
            print("3:",head.next.val)
        elif l2.next:
            head.next = l2
            print("4:",head.next.val)
        return head_node.next
"""
l1=1->2->4,l2=1->3->4
Merge = 1->1->2->3->4
2: 1
1: 1
1: 2
4: 3
"""
```

第一次的解法会丢掉最后一个值，原因在于18行的位置没有输出。因为当移至最后一个值时，`l1.next`已经为空，所以18行不会被执行。

同理，由于第5行判断条件为l1.next，所以跳出这个while循环的时候两个链表都还有值，这显然不满足后续我们想把剩余直接挂上去的条件。

### 正解

```python
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
```

