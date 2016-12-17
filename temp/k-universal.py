# encoding: utf-8

"""
@author: ferstar
@software: PyCharm Community Edition
@file: k-universal.py
@time: 2016/9/22 0:57
"""

# from multiprocessing import cpu_count
# from multiprocessing.dummy import Pool


def generate_lst(n):
    return ["0" * (n - len(bin(i)[2:])) + bin(i)[2:] for i in range(2**n)]


def generate_str(n):
    len_str = 2**n + n -1
    for i in range(2**len_str):
        yield "0" * (len_str - len(bin(i)[2:])) + bin(i)[2:]


def match_count(p, text):
    count = 0
    len_p = len(p)
    for i in range(len(text) - len_p + 1):
        if p == text[i: i + len_p]:
            count += 1
    return count

# def select_k_bin(text):
#     _lst = []
#     for k_mer in k_mers:
#         if match_count(k_mer, text) == 1:
#             _lst.append(1)
#         else:
#             _lst.append(0)
#     if all(_lst):
#         lst.append(text)


if __name__ == '__main__':
    from time import time
    t0 = time()
    k = 4
    k_mers = generate_lst(k)
    lst = []
    # pool = Pool(cpu_count())
    # pool.map(select_k_bin, generate_str(k))
    # pool.close()
    # pool.join()
    for i in generate_str(k):
        product = 1
        for k_mer in k_mers:
            if match_count(k_mer, i) == 1:
                product *= 1
            else:
                product *= 0
        if product:
            lst.append(i)
    print(lst)
    print(len(lst))
    print(time() - t0)