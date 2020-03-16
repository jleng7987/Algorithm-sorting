import numpy as np
from numpy.linalg import solve

n,k=map(int,input().split())

def getv(n,k):
    a = np.mat([[1, 1], [1, -1]])  # 系数矩阵
    b = np.mat([n, k]).T  # 常数项列矩阵
    x = solve(a, b)  # 方程组的解
    return x

count = 0

def zhaying(n,k,count):
    x = getv(n,k)
    if isinstance(int(x[0][0]), int):
        zhaying (int(x[0][0]),k,count)
        zhaying(int(x[1][0]), k, count)
    else:
        count = count + 1
        return  count

print(zhaying())