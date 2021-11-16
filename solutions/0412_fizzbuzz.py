#!/usr/bin/env python3
# https://leetcode.com/problems/fizz-buzz/
# 412. Fizz Buzz
# Easy

def fizzbuzz(n):
    words = { 3 : "Fizz", 5 : "Buzz" }
    result = []
    for i in range(1, n+1):
        place = ""
        for w in words:
            if i % w == 0:
                place += words[w]
        result.append(place or str(i))
    return result

if __name__ == "__main__":

    funct = fizzbuzz
    for ex in (
            (3, ["1", "2", "Fizz"]),
            (5, ["1", "2", "Fizz", "4", "Buzz"]),
            (15, ["1","2","Fizz","4","Buzz","Fizz","7","8", \
                    "Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]),
            ):

        print(ex[0], funct(ex[0]), ex[1] == funct(ex[0]))

