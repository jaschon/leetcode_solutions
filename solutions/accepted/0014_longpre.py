#!/usr/bin/env python3
# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/
# EASY
# Accepted
# https://leetcode.com/submissions/detail/589271587/
# 56ms (12.41%)
# 15.2MB (25.64)


from collections import Counter

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        if len(strs) == 1: return strs[0]
        parts = []
        for s in strs:
            pre = ""
            for ch in s:
                pre += ch
                parts.append(pre)
        most = ""
        c = Counter(parts)
        for v in c.elements():
            if len(v) > len(most) and c[v] == len(strs):
                most = v
        return most

if __name__ == "__main__":
    
    for example in (
            (("flower","flow","flight"), "fl"),
            (("dog", "racecar", "car"), ""),
            ((), ""),
            ([""],""),
            (["",""],""),
            (["ab", "a"], "a"),
            (["", "b"], ""),
            (["a"], "a"),
            (["reflower","flow","flight"], ""),
            (["flower","flower","flower","flower"], "flower")
            ):
        s = Solution()
        result = s.longestCommonPrefix(example[0])
        print(example[0], result, "=",  example[1], example[1] == result)
