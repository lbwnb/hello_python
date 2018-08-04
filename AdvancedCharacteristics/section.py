L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 数组下标取
print([L[0],L[1],L[2]])

# 循环取

def index(n,r=[]):
    for i in range(n):
        r.append(L[i])
    print(r)
index(2)

# 切片
print(L[0:3])
print(L[-2:])

L = list(range(100))
print(L)
# 复制一个list
print(L[:])

# tuple也可以用切片操作 操作的结果仍是tuple
print((0,1,2,3,4,5)[:3])

# 字符串也可看成一直list，每个元素就是一个字符，操作的结果仍是字符串

print('ABCDEFG'[:3])
print('ABCDEFG'[::3])

def trim(s):
    if s[:1]==" ":
        return trim(s[1:])
    elif s[-1:]==" ":
        return trim(s[:-1])
    else:
        return s

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


