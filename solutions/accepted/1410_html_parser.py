#!/usr/bin/env python3
# 1410. HTML Entity Parser
# https://leetcode.com/problems/html-entity-parser/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/612465739/
# Time: 84ms (56.84%)
# Mem: 14.6MB (97.89%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
html = { '&quot;' : '"',
        '&apos;' : "'",
        '&gt;' : '>',
        '&lt;' : '<',
        '&frasl;' : '/',
        '&amp;' : '&',
        }

class Solution:
    def entityParser(self, text: str) -> str:
        for i in html:
            text = text.replace(i, html[i])
        return text


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)

                ("&amp; is an HTML entity but &ambassador; is not.", "& is an HTML entity but &ambassador; is not."),
                ("and I quote: &quot;...&quot;", "and I quote: \"...\""),
                ("&amp;gt;", "&gt;"),

                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
