# -*- coding:utf-8 -*-

# 手写阶乘，计算C(n,m) 的值，如 C（5，3）=10

# 用python实现排列组合C(n,m) = n!/m!*(n-m)!
def get_value(n):
    if n == 1:
        return n
    else:
        return n * get_value(n - 1)
def gen_last_value(n, m):
    first = get_value(n)
    second = get_value(m)
    third = get_value((n - m))
    return first / (second * third)

if __name__ == "__main__":

    rest = gen_last_value(5, 3)
    print(int(rest))



