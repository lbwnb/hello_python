import math


def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-98))

# print(my_abs('A'))

def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny

x,y = move(100,100,60,math.pi/6)
print(x,y)


def quadratic(a,b,c):
    p=b*b-4*a*c
    if p>0:
        x1 = (-b - math.sqrt(p))/(2*a)
        x2 = (-b + math.sqrt(p))/(2*a)
        return x1,x2
    if p ==0:
        x = (-b)/(2*a)
        return x
    if p<0:
        return "无实数根"

print('quadratic(2,3,1) = ', quadratic(2,3,1))
print('quadratic(1,3,-4) = ',quadratic(1,3,-4))
print(quadratic(2,2,2))
