# encoding: utf-8

"""
@author: ferstar
@software: PyCharm Community Edition
@file: computing_frequencies.py
@time: 2016/9/12 22:59
"""


def number2symbol(n):
    """数字到基因的转换"""
    _dict = dict(zip(range(4), "ACGT"))
    if n < 4:
        return _dict.get(n)
    else:
        return number2symbol(n // 4) + _dict.get(n % 4)


def number2pattern(index, k):
    """数字到基因组合的转换"""
    if k == 1:
        return number2symbol(index)
    return number2pattern(index // 4, k - 1) + number2symbol(index % 4)


def symbol2number(s):
    """基因到数字的转换"""
    return {**dict(zip("ACGT", range(4))), **dict(zip("acgt", range(4)))}[s]


def pattern2number(p):
    """基因型到数字的转换"""
    if not p:
        return 0
    s = p[-1]
    prefix = p[:-1]
    return 4 * pattern2number(prefix) + symbol2number(s)


def computing_frequencies(text, k):
    """
    计算基因片段出现频率
    返回frequency_array
    """
    len_text = len(text)
    freq_array = [0 for _ in range(4 ** k)]
    for i in range(len_text - k + 1):
        pattern = text[i: i + k]
        j = pattern2number(pattern)
        freq_array[j] += 1
    return freq_array


def faster_frequent_words(text, k):
    freq_ps = set()
    freq_array = computing_frequencies(text, k)
    max_count = max(freq_array)
    for i in range(4**k):
        if freq_array[i] == max_count:
            freq_ps.add(number2pattern(i, k))
    return freq_ps, max_count


def better_clump_finding(genome, k, l, t):
    frequent_patterns = set()
    # clumps = [0 for _ in range(4**k)]
    text = genome[:l]
    frequent_array = computing_frequencies(text, k)
    clumps = list(map(lambda _: 1 if frequent_array[_] >= t else 0, (0 for _ in range(4**k))))
    for i in range(1, len(genome) - l + 1):
        first_pattern = genome[i - 1: i + k -1]
        index = pattern2number(first_pattern)
        frequent_array[index] -= 1
        last_pattern = genome[i + l - k: i + l]
        index = pattern2number(last_pattern)
        frequent_array[index] += 1
        if frequent_array[index] >= t:
            clumps[index] = 1
    for i, j in enumerate(clumps):
        if j == 1:
            frequent_patterns.add(number2pattern(i, k))
    return frequent_patterns


def frequency_dict(text, k):
    _dict = dict()
    for i in range(len(text) - k + 1):
        pattern = text[i: i + k]
        if _dict.get(pattern):
            _dict[pattern] += 1
        else:
            _dict[pattern] = 1
    return _dict


def better_clump_finder(genome, k, l, t):
    _set = set()
    _text = genome[:l]
    _dict = frequency_dict(_text, k)
    for i in _dict:
        if _dict[i] >= t:
            _set.add(i)
    for i in range(1, len(genome) - l + 1):
        _pattern = genome[i - 1: i - 1 + k]
        _dict[_pattern] -= 1
        pattern_ = genome[i + l - k: i + l]
        if _dict.get(pattern_):
            _dict[pattern_] += 1
        else:
            _dict[pattern_] = 1
        if _dict[pattern_] >= t:
            _set.add(pattern_)
    return _set

if __name__ == '__main__':
    print(faster_frequent_words("CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA", 3))