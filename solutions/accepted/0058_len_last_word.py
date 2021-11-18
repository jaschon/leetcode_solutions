#!/usr/bin/env python3
#https://leetcode.com/problems/length-of-last-word/
# 58. Length of Last Word
# Easy
# Accepted
# https://leetcode.com/submissions/detail/589206772/
# 32ms (59.83%)
# 14.2 MB (87.83%)


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

if __name__ == "__main__":

    for ex in (
            ("Hello World", 5),
            ("   fly me   to   the moon  ", 4),
            ("luffy is still joyboy", 6),
            ):
        s = Solution()
        print(ex[0], s.lengthOfLastWord(ex[0]), ex[1] == s.lengthOfLastWord(ex[0]))

