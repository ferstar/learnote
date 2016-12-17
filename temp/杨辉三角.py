#!/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 18:01:41 2016

@author: ferstar
"""

def triangles():
    a = [1]
    while 1:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]
    

def main():
    n = 0
    for t in triangles():
        print(t)
        n = n + 1
        if n == 10:
            break

if __name__ == "__main__":
    main()
