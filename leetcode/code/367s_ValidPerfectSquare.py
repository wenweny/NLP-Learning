# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/11/4 9:19
# @Author  : yangwenwen
# @Function: leetcode 367

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


class Solution11:
    def isPerfectSquare(self, num: int) -> bool:
        """ 二分查找 """
        left = 0
        right = num // 2
        i = 1
        while left < i <= right:
            multiply_num = i * i
            if multiply_num == num:
                return True
            elif multiply_num < num:
                l = i
                i = (left + right) // 2
            elif multiply_num > num:
                left = i
                i = (left + right) // 2
        return False


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


print(Solution().isPerfectSquare(9))
