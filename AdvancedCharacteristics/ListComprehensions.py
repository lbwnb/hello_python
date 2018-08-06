import os

a=list(range(1,11))

L =[]
for x in range(1,11):
    L.append(x * x)

print(L)

# 列表生成式，生成的元素x*x  for循环  可以接条件
Q = [x*x for x in range(1,11) if x % 2 == 0]
print(Q)

# 两层循环，生成全排列
E = [m + n for m in 'ABC' for n in 'XYZ']
print(E)

# 列出当前目录下的所有文件和目录名
R = [d for d in os.listdir('.')]
print(R)

c = {'x':'A','y':'B','z':'C'}
for k,v in c.items():
    print(k,'=',v)




d = {'x':'A','y':'B','z':'C'}
W = [k + '=' + v for k,v in d.items()]
print(W)

L = ['Hello','World','IBM','Apple']
P = [s.lower() for s in L]
print(P)


# 修改列表生成式，通过添加if语句保证列表生成式能正确地执行
L1 = ['Hello','World',18,'Apple',None]
L2 = [s.lower()for s in L1 if isinstance(s,str)]
