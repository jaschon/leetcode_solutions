#!/usr/bin/env python3
# 929. Unique Email Addresses
# https://leetcode.com/problems/unique-email-addresses/
# Easy

# Accepted 
# Result: https://leetcode.com/submissions/detail/599000118/
# Time: 40ms (99.13%)
# Mem: 14.4MB (62.57%)

import sys
sys.path.insert(0,'..')
from _helper import *


class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        results = set()
        for e in emails:
            l, d = e.split("@")
            results.add(f'{l.split("+")[0].replace(".", "")}@{d}')
        return len(results)


if __name__ == "__main__":
    for e in (

            (["test.email+alex@leetcode.com","test.email.leet+alex@code.com"], 2),
            (["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"], 2),
            (["a@leetcode.com","b@leetcode.com","c@leetcode.com"], 3),

            ):

        funct = Solution().numUniqueEmails

        print()

        test(funct, e[1], e[0])
        timer(funct, e[0])

        print()
