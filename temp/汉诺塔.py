#!/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 09:56:30 2016

@author: ferstar
"""
lst = []

def move(n, a, b, c):
    if n == 1:
        lst.append("{}-->{}".format(a, c))
    else:
        move(n-1, a, c, b)
        lst.append("{}-->{}".format(a, c))
        move(n-1, b, a, c)

def main():
    move(3, "A", "B", "C")
    for i in lst:
        print(i)
    print("总共需要{}步".format(len(lst)))

if __name__ == "__main__":
    main()
