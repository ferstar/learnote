def get_odd():  # 初始化一个从3开始的奇数序列
    n = 1
    while 1:
        n += 2
        yield n


def not_divisible(n):  # 筛选函数, 过滤掉被前一项整除的元素
    return lambda x: x % n > 0


def primes():
    yield 2  # 返回第一个素数
    it = get_odd()  # 初始化序列, 这是个无限序列
    while 1:
        n = next(it)  # 返回序列第一个值
        yield n  # 第一个值为3, 也是素数
        it = filter(not_divisible(n), it)  # 构造新序列, 用第一个元素分别整除新序列每一项


for n in primes():
    if n < 100:  # 打印100以内的素数
        print(n)
    else:
        break
