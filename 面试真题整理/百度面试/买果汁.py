n,k=map(int,input().split())
a = list(map(int, input().split()))
def guozhi(a):
    dict = {}
    for key in a:
        dict[key] = dict.get(key, 0) + 1
    return dict
def zc(b):
    if (b % 2) == 0:
        return b/2
    else:
        return (b+1)/2
d = guozhi(a)
count = 0
for  key in d:
    count = count + zc(d[key])
print(int(count))

