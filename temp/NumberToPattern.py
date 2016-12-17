# encoding: utf-8

"""
@author: ferstar
@software: PyCharm Community Edition
@file: NumberToPattern.py
@time: 2016/9/12 22:07
"""

import sys


def n2s(n):
    new_dict = dict(zip(range(4), "ACGT"))
    if n < 4:
        return new_dict.get(n)
    else:
        return n2s(n // 4) + new_dict.get(n % 4)


def NumberToPattern(index, k):
    if k == 1:
        return n2s(index)
    return NumberToPattern(index // 4, k-1) + n2s(index % 4)


if __name__ == '__main__':
    print(NumberToPattern(8320, 7))