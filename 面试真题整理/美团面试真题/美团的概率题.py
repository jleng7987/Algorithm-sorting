from itertools import permutations, combinations

N = int(input())
a = list(map(int, input().split()))

def huanwei(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def findMod(a, m):  # 这个扩展欧几里得算法求模逆
    if huanwei(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


def EX_GCD(a,b,arr): #扩展欧几里得
    if b == 0:
        arr[0] = 1
        arr[1] = 0
        return a
    g = EX_GCD(b, a % b, arr)
    t = arr[0]
    arr[0] = arr[1]
    arr[1] = t - int(a / b) * arr[1]
    return g
def ModReverse(a,n): #ax=1(mod n) 求a模n的乘法逆x
    arr = [0,1,]
    gcd = EX_GCD(a,n,arr)
    if gcd == 1:
        return (arr[0] % n + n) % n
    else:
        return -1


def lingci(N, a):
    d0 = 1
    for i in range(N):
        d0 *= 1.0 / a[i]
    return d0

def yici(N, a):
    gailv = 0
    for i in range(0, len(a)):
        b = a[:i]+a[i+1:]
        gailv = gailv + lingci(N - 1, b) * (1 - 1 / a[i])
    return gailv


def erci(N, a):
    gailv = 0
    gailv2 = []
    for i in range(0, len(a)):
        b = a[:i] + a[i + 1:]
        gailv1 = yici(N-1,b)
        gailv2.append(gailv1*(1-1/a[i]))
        print("yici:",gailv1)
        # for j in range(0, len(b)):
        #     c = b[:i] + b[i + 1:]
        #     d = yici(N - 2, c)
        #     print('erci',d)
        #     gailv2.append(gailv1*d)
        print("gailv2:",gailv2)

    return sum(gailv2)/2

a1 = 1 / lingci(N, a)
# a11 = int(findMod(a1, 998244353))
print(1/a1)
b = 1 / yici(N, a)
print(1/b)
# b1 = int(findMod(b, 998244353))

c = 1 / erci(N, a)
print(1/c)
# c1 = int(ModReverse(c, 998244353))
print(1/a1, 1/b , 1/c)
# print(a11, b1 , c1)