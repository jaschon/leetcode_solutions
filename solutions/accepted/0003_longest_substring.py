#!/usr/bin/env python3
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 3. Longest Substring Without Repeating Characters
# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/598384386/
# Time: 57ms (54.25%)
# Mem: 14.4MB (30.21%)

import sys
sys.path.insert(0,'..')
from _helper import *


class Solution:
    def lengthOfLongestSubstring(self, s):
        last = {}
        maxlen = 0
        start = 0
        for i in range(0, len(s)):
            if s[i] in last:
                start = max(start, last[s[i]]+1)
            maxlen = max(maxlen, i-start+1)
            last[s[i]] = i
        return maxlen



if __name__ == "__main__":
    for e in (
            ("abcabcbb", 3),
            ("bbbbb", 1),
            ("pwwkew", 3),
            ("", 0),
            ):

        funct = Solution().lengthOfLongestSubstring

        test(funct, e[1], e[0])
        timer(funct, e[0])

        print()
