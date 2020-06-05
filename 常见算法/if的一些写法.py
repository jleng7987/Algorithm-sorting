# 实现函数效果
def pandaun(age):
    if age > 18:
        return "已成年"
    else:
        return "未成年"


age1 = 20
age2 = 17

# 语法一
# <expression 1> if <condition> else <expression 2>

msg1 = "已成年" if age1 > 18 else "未成年"
print(msg1)

# 语法二
# <expression> and <on_true> or <on_false>
msg1 = age1 > 18 and "已成年" or "未成年"


# 语法三
# ("false", "true")[condition]
msg1 = ("未成年", "未成年")[age1 > 18]

# 语法四
# (lambda: <on_false>, lambda:<on_true>)[<condition>]()
msg1 = (lambda:"未成年", lambda:"已成年")[age1 > 18]()

# 语法五
# {True: <on_true>, False: <on_false>}[<condition>]
msg1 = {True: "已成年", False: "未成年"}[age1 > 18]

# 语法六
# ((<condition>) and (<on_true>,) or (<on_false>,))[0]
msg1 = ((age1 > 18) and ("已成年",) or ("未成年",))[0]