n = int(input())
a = list(map(int, input().split()))
count0 = 0
count1 = 1
count2 = 2
for i in a:
    if i == 0:
        count0 = count0 + 1
    elif i == 1:
        count1 = count1 + 1
    else:
        count2 = count2 + 1
if count0 ==n:
    print(int(0))
elif count1==n:
    b = (1+n)*n/2
    print(int(b))
elif count2==1:
    b = (1 + n) * n / 2
    index = 0
    for i in a:
        index = index +1
        if i == 2:
            break
    c = (1 + index) * index / 2
    print(int(b/2+c/2))
elif count1==1:
    b = (1 + n) * n / 2
    index = 0
    for i in a:
        index = index +1
        if i == 1:
            break
    c = (1 + index) * index / 2
    print(int(b/2+c/2))