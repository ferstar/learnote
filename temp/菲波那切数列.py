#!/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 18:35:40 2016

@author: ferstar
"""
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1
    return "done"


def main():
    fib(10)

if __name__ == "__main__":
    main()
