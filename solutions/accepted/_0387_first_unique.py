#!/usr/bin/env python3
# 387. First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/
# Accepted!
# 60ms (97.66%)
# 14.6MB (21.25%)


from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for c in counter:
            if counter[c] == 1:
                return s.index(c)
        return -1



if __name__ == "__main__":
    for ex in (
            ("leetcode", 0),
            ("loveleetcode", 2)

            ):
        result = Solution().firstUniqChar(ex[0])
        print(ex[0], result, "PASS" if result == ex[1] else "FAIL")


