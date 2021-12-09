#!/usr/bin/bash

# 195. Tenth Line
# https://leetcode.com/problems/tenth-line/
# Easy

# Accepted
# 4ms (82.13%)
# 3.6MB (31.03%)

head -n 10 file.txt | tail -n +10
