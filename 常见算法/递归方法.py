
# 类似与栈的先进后出模式

# 递归的两个必要条件
# 1.要有递推关系
# 2.要有临界
def digui(num):
    print('$' + str(num))
    # 临界值
    if num > 0:
        # 这里用的是调用本身的函数(递推关系)
        digui(num - 1)
    else:
        print('=' * 20)
    print(num)


digui(3)