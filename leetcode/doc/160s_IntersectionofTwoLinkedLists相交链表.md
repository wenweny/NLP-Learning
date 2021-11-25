> [leetcode160 简单题 相交链表](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/)

## 题目描述

给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。

题目数据 保证 整个链式结构中不存在环。

注意，函数返回结果后，链表必须 保持其原始结构 。

较多图片描述，可跳至[链接](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/)查看详细描述。

进阶：你能否设计一个时间复杂度 O(n) 、仅用 O(1) 内存的解决方案？

## 解题

如下图所示有两个链表

- `A：a1->a2->c1->c2`
- `B：b1->b2->b3->c1->c2`

如果用两个指针p1和p2分别在两条链表上前进，并不能同时走到公共节点，也就无法得到相交节点c1。所以，解决这个问题的关键是，通过某些方式，让p1和p2能够同时到达相交节点c1。

所以，我们可以让p1遍历完链表A之后开始遍历链表B，让p2遍历完链表B之后开始遍历链表A，这样相当于「逻辑上」两条链表接在了一起。

如果这样进行拼接，就可以让p1和p2同时进入公共部分，也就是同时到达相交节点。

![image-20211124140955366](E:\codeproject\NLP-Learning\leetcode\doc\image\160相交链表.jpg)

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
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

```

**注意：是转到B链表，不是让`p.next=headB`**

## 参考资料

https://labuladong.gitee.io/algo/2/17/16/
