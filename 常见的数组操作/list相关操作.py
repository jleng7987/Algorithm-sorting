# list的切片
# 切片时遵循“包头不包尾”的原则，
listtest1 = [1,2,3,4,5,6]
print(listtest1[:3])
# [1, 2, 3]
print(listtest1[6:])
#[]

# 利用切片获取listtest1[i]和剩下的部分
for i in range(0,len(listtest1)):
    a = listtest1[i]
    b = listtest1[:i] + listtest1[i+1:]
    print(a)
    print(b)
