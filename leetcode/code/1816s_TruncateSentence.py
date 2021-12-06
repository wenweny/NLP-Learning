# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/12/6 18:52
# @Author  : yangwenwen
"""
@Function: 
句子 是一个单词列表，列表中的单词之间用单个空格隔开，且不存在前导或尾随空格。每个单词仅由大小写英文字母组成（不含标点符号）。

例如，"Hello World"、"HELLO" 和 "hello world hello world" 都是句子。
给你一个句子 s​和一个整数 k​，请你将 s​截断 ​，​​​使截断后的句子仅含 前 k​个单词。
返回 截断 s​后得到的句子。
 

示例 1：

输入：s = "Hello how are you Contestant", k = 4
输出："Hello how are you"
解释：
s 中的单词为 ["Hello", "how" "are", "you", "Contestant"]
前 4 个单词为 ["Hello", "how", "are", "you"]
因此，应当返回 "Hello how are you"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/truncate-sentence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # 其实用split就够了
        # res_list = s.split(" ")[:k]
        # return " ".join(res_list)

        # 不用list，也不需要全部遍历完
        count = 0
        # 要考虑到字符串走到最后一位，列表截断左闭右开
        for idx, s_char in enumerate(s):
            if s_char == " " or idx == len(s) - 1:
                count += 1
            if count == k:
                if idx == len(s) - 1:
                    return s[:idx + 1]
                else:
                    return s[:idx]


# "Hello how are you"
print(Solution().truncateSentence(s="chopper is not a tanuki", k=4))
