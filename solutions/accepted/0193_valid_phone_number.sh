# 193. Valid Phone Numbers
# https://leetcode.com/problems/valid-phone-numbers/
# Easy

# Accepted
# 3.1 MB (47.84%)
# https://leetcode.com/submissions/detail/599413393/

# file.txt
# 987-123-4567
# 123 456 7890
# (123) 456-7890
# 123-456-7891

grep -e "^([0-9]\{3\}) [0-9]\{3\}-[0-9]\{4\}$\|^[0-9]\{3\}\-[0-9]\{3\}-[0-9]\{4\}$" file.txt 
