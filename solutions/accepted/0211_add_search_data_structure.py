#!/usr/bin/env python3
# 211. Design Add and Search Words Data Structure
# https://leetcode.com/problems/design-add-and-search-words-data-structure/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/631736707/
# Time: 3964 ms (5.01%)
# Mem: 29.1MB (25.80%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List

### ADD SOLUTION CLASS HERE 

class Node:
    def __init__(self, char="", full=""):
        self.children = []
        self.char = char
        self.full = [full,]

class WordDictionary:

    def __init__(self):
        self.root = Node()
        self.matches = []
        self.search_word = ""
        self.kill = False

    def addWord(self, word: str) -> None:
        def add(word, full="", node=None):
            if not word: 
                return
            if not node.children:
                new = Node(word[0], full)
                node.children.append(new)
                add(word[1:], full, new)
                return
            else:
                for child in node.children:
                    if child.char == word[0]:
                        child.full.append(full)
                        add(word[1:], full, child)
                        return
                new = Node(word[0], full)
                node.children.append(new)
                add(word[1:], full, new)
        add(word, word, self.root)

    def search(self, word: str) -> bool:
        def find(word, node=None):
            if self.kill: return
            for child in node.children:
                if word[0] in (child.char, "."):
                    if len(word) > 1 and child.children:
                        find(word[1:], child)
                    elif len(word) == 1 and (child.char in child.full or self.search_word in child.full or not child.children):
                        self.matches.append(child.full)
                        self.kill = True

        self.matches = []
        self.kill = False
        self.search_word = word 
        find(word, self.root)
        return bool(self.matches)


if __name__ == "__main__":
    d = WordDictionary()
    d.addWord("a")
    d.addWord("ab")
    # print(d.root.children[0].children[0].char)
    for t in (
            ("a", True),
            ("ab", True),
            (".a", False),
            (".a", False),
            (".b", True),
            ("ab.", False),
            (".", True),
            ("..", True),

    ):

        print("")
        test(d.search, t[-1], t[0])
        print("")


