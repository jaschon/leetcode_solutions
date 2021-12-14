#!/usr/bin/env python3

# 68. Text Justification
# https://leetcode.com/problems/text-justification/

# Hard

# Accepted
# Result:  https://leetcode.com/submissions/detail/601945087/
# Time: 33ms (28.38%)
# Mem: 14.3 MB (79.50%)

import sys
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution:

    def space(self, words, maxLen):
        count = maxLen - sum(len(i) for i in words) 
        if " " in words:
            while count > 0:
                for i in range(len(words)):
                    if words[i].startswith(" "):
                        words[i] = words[i] + " "
                        count -= 1
                        if count == 0: break
                    elif len(words[i]) == maxLen:
                        continue
        return "".join(words)

    def split(self, words, maxWidth):
        lines = []
        line = []
        count = 0
        while words:
            word = words.pop()
            if len(word)+count > maxWidth:
                words.append(word)
                if len(line) > 2:
                    lines.append(line[0:-1])
                else:
                    lines.append(line)
                count = 0
                line = []
            else:
                line.append(word)
                count += len(word)
                if len(word) < maxWidth or count < maxWidth:
                    line.append(" ")
                    count += 1
        if line:
            lines.append(line)
        return lines

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        ws = self.split(words[::-1], maxWidth)
        for i, w in enumerate(ws):
            if i+1 == len(ws):
                if w[-1] == " ":
                    w.pop()
                result.append("".join(w).ljust(maxWidth))
                print(len(result[-1]))
            else:
                result.append(self.space(w, maxWidth))
        return result




if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution().fullJustify,
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)


                (["This", "is", "an", "example", "of", "text", "justification."], 16, 
                    ["This    is    an","example  of text","justification.  "]
                    ),
                (["What","must","be","acknowledgment","shall","be"], 16, []),

               (["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"], 16, 
                   ["ask   not   what","your country can","do  for  you ask","what  you can do","for your country"]),


                ):

            funct = f
            print()

            ### ADD EXTRA PARAM AFTER e[0]...
            test(funct, e[-1], e[0], e[1])

            ### NODE VERSION OF TEST
            # test_node(funct, cmp, val)

            # timer(funct, e[0])
            # timer_amt(funct, 10, e[0])

            print()
