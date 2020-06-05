import random
def random01():
    i = [random.random() for i in range(1)]
    return i

def input(n):
    list1 = []
    for i in range(n):
        list1.append(random01)
    a = sum(list1)
    if a == 0:
        return True
    else:
        return False
print(input(10))