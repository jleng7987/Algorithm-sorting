import math
n=int(input())
ls = []
lsd = []
for i in range(0,n):
    c, k = map(int, input().split())
    d = (math.pow(c, 2) + math.pow(k, 2)) ** 0.5
    ls.append([c,k])

# ls1 = set(ls)
# ls1.sort(reverse=True)
print(ls)
def minl (i, min, count=0):
    if i == n:
        return count
    if ls[i][0] > min[0] & ls[i][1] > min[1]:
        min = ls[i]
        count = count +1
        minl(i+1,min,count)
    else:
        minl(i+1,min,count)
ls2 = []
for i in range(0,n):
    minbox = [0][0]
    count1 = minl(0, minbox)
    ls2.append(count1)

print(ls2)

