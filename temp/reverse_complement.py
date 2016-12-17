# encoding: utf-8

"""
@author: ferstar
@software: PyCharm Community Edition
@file: reverse_complement.py
@time: 2016/9/13 0:38
"""


def reverse_complement(pattern):
    new_dict = dict(zip("ACGT", "TGCA"))
    return "".join((new_dict[pattern[i]] for i in range(len(pattern))))[::-1]


def count_index(p, g):
    for i in range(len(g) - len(p) + 1):
        if g[i: i+len(p)] == p:
            print(i, end=" ")

# with open("Vibrio_cholerae.txt", "r") as fh:
#     line = fh.readline().strip()
#     count_index("ATGATCAAG", line)
#     print("\n")
#     count_index("CTTGATCAT", line)

print(reverse_complement("TTGTGTC"))