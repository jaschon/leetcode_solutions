#!/usr/bin/env python3
# 535. Encode and Decode TinyURL
# https://leetcode.com/problems/encode-and-decode-tinyurl/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/631818669/
# Time: 44ms (45.16%)
# Mem: 14.2MB (76.34%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
import random
from string import ascii_letters, digits
class Codec:
    url2tiny, tiny2url = {},{}
    chars = ascii_letters+digits
    
    def gen(self):
        return "http://tinyurl.com/" + "".join(random.choice(self.chars) for _ in range(6))
    
    def make(self):
        while True:
            gen = self.gen()
            if not gen in self.tiny2url:
                return gen
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.url2tiny:
            return self.url2tiny[longUrl]
        self.url2tiny[longUrl] = self.make()
        self.tiny2url[self.url2tiny[longUrl]] = longUrl
        return self.url2tiny[longUrl]
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.tiny2url.get(shortUrl, "")  



if __name__ == "__main__":
    pass

