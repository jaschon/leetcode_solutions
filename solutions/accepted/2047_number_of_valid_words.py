#!/usr/bin/env python3

# 2047. Number of Valid Words in a Sentence
# https://leetcode.com/problems/number-of-valid-words-in-a-sentence/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/661898847/
# Time: 52ms (75.37%)
# Mem: 14MB (37.55%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
from collections import Counter
class Solution:
    def countValidWords(self, sentence: str) -> int:
        result = 0
        alpha = set("abcdefghijklmnopqrstuvwxyz")
        punct = set("-!.,")

        for word in sentence.split():
            wordset = set(word)
            other = wordset-alpha

            #detect just alpha. count if true
            if len(other) == 0:
                result += 1
                continue

            #detect numbers. skip if found
            if len(other-punct) > 0:
                continue


            c = Counter(word)
            is_good = True

            for char in other:
                if c[char] > 1:
                    is_good = False
                    break
                if char == "-":
                    if word[0] == char or word[-1] == char:
                        is_good = False
                    else:
                        index = word.index(char)
                        if word[index-1] in punct or word[index+1] in punct:
                            is_good = False
                elif char != word[-1]:
                    is_good = False
                    break

            if is_good:
                result += 1

        return result



            







if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                # ("cat and  dog", 3),
                # ("!this 1-s b8d!", 0),
                # ("this-should pass", 2),
                # ("-fail", 0),
                # ("p-ass", 1),
                # ("fail-", 0),
                # ("f!ail", 0),
                # ("!fail", 0),
                # ("pass!", 1),
                # ("alice and  bob are playing stone-game10", 5),
                (" 62   nvtk0wr4f  8 qt3r! w1ph 1l ,e0d 0n 2v 7c.  n06huu2n9 s9   ui4 nsr!d7olr  q-, vqdo!btpmtmui.bb83lf g .!v9-lg 2fyoykex uy5a 8v whvu8 .y sc5 -0n4 zo pfgju 5u 4 3x,3!wl  fv4   s  aig cf j1 a i  8m5o1  !u n!.1tz87d3 .9    n a3  .xb1p9f  b1i a j8s2 cugf l494cx1! hisceovf3 8d93 sg 4r.f1z9w   4- cb r97jo hln3s h2 o .  8dx08as7l!mcmc isa49afk i1 fk,s e !1 ln rt2vhu 4ks4zq c w  o- 6  5!.n8ten0 6mk 2k2y3e335,yj  h p3 5 -0  5g1c  tr49, ,qp9 -v p  7p4v110926wwr h x wklq u zo 16. !8  u63n0c l3 yckifu 1cgz t.i   lh w xa l,jt   hpi ng-gvtk8 9 j u9qfcd!2  kyu42v dmv.cst6i5fo rxhw4wvp2 1 okc8!  z aribcam0  cp-zp,!e x  agj-gb3 !om3934 k vnuo056h g7 t-6j! 8w8fncebuj-lq    inzqhw v39,  f e 9. 50 , ru3r  mbuab  6  wz dw79.av2xp . gbmy gc s6pi pra4fo9fwq k   j-ppy -3vpf   o k4hy3 -!..5s ,2 k5 j p38dtd   !i   b!fgj,nx qgif ", 49),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            # timer(funct, 5, *e[:-1])


            print()
