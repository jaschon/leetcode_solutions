#!/usr/bin/env python3
# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
# Medium
# Accepted!
# https://leetcode.com/problems/longest-palindromic-substring/submissions/
# 5148ms (21.37%)
# 14.4 MB (35.95%)

class Solution:
    def longestPalindrome(self, s=""):
        longest = 0
        result = ""
        for i in range(len(s)+1):
            for j in reversed(range(len(s))):
                if s[i] != s[j] or j < i or (j-i) < longest:
                    continue
                sub = s[i:j+1]
                if sub == sub[::-1] and len(sub) > longest:
                    result = sub
                    longest = len(sub)
        return result

if __name__ == "__main__":
    for ex in (
            ("babad", "bab"),
            ("cbbd", "bb"),
            ("a", "a"),
            ("ac", "a"),
            (" ", " "),
            ("", ""),
            ):
        result = Solution().longestPalindrome(ex[0])
        print(ex[0], result, '--', ex[1] == result)
