# Valid Perfect Square 有效的完全平方数

> leetcode 367 简单题 [Valid Perfect Square](https://leetcode-cn.com/problems/valid-perfect-square/)



给定一个 **正整数** num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。

**进阶：不要** 使用任何内置的库函数，如  sqrt 。

**示例 1：**

```txt
输入：num = 16
输出：true
```

**示例 2：**

```
输入：num = 14
输出：false
```

**提示：**

1 <= num <= 2^31 - 1

## 解法

**1.自己想的 过分暴力法**

```python
class Solution2:
    """
    过分暴力法，测试用例超时
    """

    def isPerfectSquare(self, num: int) -> bool:
        # 错误写法：num == 1 or 4 等同于 (num==1) or 4
        # 错误写法：num == (1 or 4) 括号内的值永远为1
        if (num == 1) or (num == 4):
            print(num)
            return True
        for i in range(num // 2):
            if i * i == num:
                print(i)
                return True
        return False
```

**2.正确的暴力遍历法**

```python
class Solution1:
    def isPerfectSquare(self, num: int) -> bool:
        """
        正确暴力法
        不需要算到num//2,当有数字相乘>num即可停止
        """
        multiply_num = 0
        i = 0
        while multiply_num < num:
            multiply_num = i * i
            if multiply_num == num:
                print(i)
                return True
            else:
                i += 1
        return False
```

**3.正解**

```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        二分查找，终止条件是左边小于等于右边
        :param num: 
        :return: 
        """
        left, right = 0, num
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square < num:
                left = mid + 1
            elif square > num:
                right = mid - 1
            else:
                return True
        return False
```

