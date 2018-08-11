L = [x*x for x in range(10)]
print(L)
g = (x*x for x in range(10))
print(next(g))

for n in g:
    print(n)
# 斐波拉契

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b , a+b
        n = n + 1
    return 'done'

print(fib(10))

# t是一个TUPLE

def fib1(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b , a + b
        n = n + 1
    return 'done'
# fot循环代替取值
for n in fib1(6):
    print(n)

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)

o = odd()
next(o)
next(o)
next(o)
next(o)


# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
c = fib1(6)
while True:
    try:
        x = next(c)
        print(':',x)
    except StopAsyncIteration as e:
        print('Generator return value', e.value)
        break




def triangles():
    L1 = [1]
    while True:
        yield L1
        if len(L1) == 1:
             L1=L1+[1]
        else:
            L1= [L1[x]+L[x+1] for x in range(len(L1)-1)]
            L1.insert(0,1)
            L1.append(1)

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')