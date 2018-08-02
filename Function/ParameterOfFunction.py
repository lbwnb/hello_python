def power(x,n=2):
    s=1
    while n>0:
        n = n-1
        s = s*x
    return s
a=power(5)
print(a)

def enroll(name,gender,age=6,city="BeiJing"):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city',city)

enroll('Sarah','F')
enroll('Bob','M',7)
enroll('Adam','M',city='TianJin')

def add_end(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L

b=add_end([1,2,3])
print(b)
c = add_end()
print(c)
d =add_end()
print(d)

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
e = calc([1,2,3])
print(e)
f = calc((1,8,6,9))
print(f)

def calc1(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
g = calc1(1,2)
print(g)

name = [1,2,3,4,5]
a1 = calc1(*name)
print(a1)

def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
person('Michhael',30)
person('Bod',35,city='BeiJing')

extra = {'city':'BeiJing','job':'Engineer'}
person('Jack',24,city=extra['city'],job=extra['job'])
person('Jack',24,**extra)

def person1(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:',name,'age:',age,'other:',kw)
person1('Jack',24,city="BeiJing",addr='Chaoyang',zipcode=123456)

def person2(name,age,*,city,job):
    print(name,age,city,job)

person2('Jack',24,city='BeiJing',job='Engineer')

# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
def f2(a,b,c=0,*,d,**kw):
    print('a=', a, 'b=', b, 'c=', c, 'd=',d, 'kw=', kw)

f1(1,2)
f1(1,2,c=3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x=99)
args=(1,2,3,4)

kw = {'d':9,'x':'#'}
f1(*args,**kw)

def product(x,*number):
    if number ==():
        return x
    else:
        for n in number:
            x = n * x
            print(x)


product(5,6,7,8)

