# 递归计算阶乘
def fact(n):
    if n ==1:
        return 1
    return n * fact(n - 1)
a=fact(500)
print(a)

# 尾递归优化

def fact(n):
    return facct_item(n,1)

def facct_item(num, product):
    if num == 1:
        return product
    return facct_item(num-1,num*product)
a = fact(500)
print(a)

# 递归完成汉诺塔的移动
def move(n,a,b,c):
    if n==1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        print(a,'-->',c)
        move(n-1,b,a,c)
move(3,'a','b','c')
