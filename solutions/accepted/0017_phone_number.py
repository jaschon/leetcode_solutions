#!/usr/bin/env python3
# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Medium
# Accepted!
# https://leetcode.com/submissions/detail/594499901/
# 32ms (68.02%)
# 14.3 (64.49%)

MAP = ("", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz")

class Counter:

    def __init__(self, digits):
        self.digits = [int(_) for _ in digits]
        self.arr = [MAP[_] for _ in self.digits]
        self.index = [0 for d in digits]
        self.go = True if digits else False

    def inc(self):
        self.index[0] += 1
        for i in range(len(self.index)):
            try:
                if self.index[i] > 2:
                    if (self.digits[i] == 7 or self.digits[i] == 9) and self.index[i] == 3:
                        continue
                    self.index[i] = 0
                    self.index[i+1] += 1
            except IndexError:
                self.go = False

    def get(self):
        result = ""
        for i in range(len(self.index)):
            result += self.arr[i][self.index[i]]
        return result


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        result = []
        c = Counter(digits)
        while c.go:
            result.append(c.get())
            c.inc()
        return result



            
if __name__ == "__main__":
    for ex in (
            ("", []),
            ("9", ["w", "x", "y", "z"]),
            ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
            ("234", ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"]),
            ("2", ["a", "b", "c"]),
            ("5678", ["jmpt","jmpu","jmpv","jmqt","jmqu","jmqv","jmrt","jmru","jmrv","jmst","jmsu","jmsv","jnpt","jnpu","jnpv","jnqt","jnqu","jnqv","jnrt","jnru","jnrv","jnst","jnsu","jnsv","jopt","jopu","jopv","joqt","joqu","joqv","jort","joru","jorv","jost","josu","josv","kmpt","kmpu","kmpv","kmqt","kmqu","kmqv","kmrt","kmru","kmrv","kmst","kmsu","kmsv","knpt","knpu","knpv","knqt","knqu","knqv","knrt","knru","knrv","knst","knsu","knsv","kopt","kopu","kopv","koqt","koqu","koqv","kort","koru","korv","kost","kosu","kosv","lmpt","lmpu","lmpv","lmqt","lmqu","lmqv","lmrt","lmru","lmrv","lmst","lmsu","lmsv","lnpt","lnpu","lnpv","lnqt","lnqu","lnqv","lnrt","lnru","lnrv","lnst","lnsu","lnsv","lopt","lopu","lopv","loqt","loqu","loqv","lort","loru","lorv","lost","losu","losv"]),
            ):
        result = Solution().letterCombinations(ex[0])
        test_len = (len(result) == len(ex[1]))
        test_cmp = True
        for r in result:
            if not r in ex[1]:
                test_cmp = False
                break
        print(ex[0], result, "PASS" if (test_len and test_cmp) else "FAIL")


