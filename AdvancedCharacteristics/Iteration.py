d={'a':1,'b':2,'c':3}
for key in d:
    print(key)

for ch in 'ABC':
    print(ch)

for i,value in enumerate(['A','B','C']):
    print(i,value)

for x,y in[(1,1),(2,4),(3,8)]:
    print(x,y)
def findMinAndMax(L):
    if len(L)>0:
        min,max=L[0],L[0]
        for i in L:
            if i<min:
                min = i
            if i>max:
                max = i
        return min,max
    else:
            return (None,None)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')









