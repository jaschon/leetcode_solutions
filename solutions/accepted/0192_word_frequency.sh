#!/usr/bin/bash

# 192. Word Frequency
# Medium
# https://leetcode.com/problems/word-frequency/

# Accepted
# 0ms (100%???)
# 3.9MB (49.30%)
# https://leetcode.com/submissions/detail/599502359/

# words.txt
# the day is sunny the the
# the sunny is is

cat words.txt | tr ' ' '\n' | sort | sed '/^$/d' | uniq -c | sort -nr | awk  '{print $2 " " $1}'
