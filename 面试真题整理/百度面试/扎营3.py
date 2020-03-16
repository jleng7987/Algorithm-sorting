n,k=map(int,input().split())
count = []
def zhaying(n,k,count):
    if n <= k & n !=0:
        count.append(1)
        return count
    elif n == 0:
        return  count
    x = (n - k) / 2
    zhaying(int(x) + k, k, count)
    zhaying(int(x), k, count)

    # if  type(x) == int:
    #     zhaying(x+k, k, count)
    #     zhaying(x, k, count)
    # else:
    #     zhaying(int(x) + k, k, count)
    #     zhaying(int(x), k, count)
    return count
print(sum(zhaying(n,k,count)))