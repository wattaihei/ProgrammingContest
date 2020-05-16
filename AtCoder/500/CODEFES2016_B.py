x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

def cos(x1, y1, x2, y2, x3, y3):
    x2 -= x1
    x3 -= x1
    y2 -= y1
    y3 -= y1
    return (x2*x3+y2*y3)/((x2**2+y2**2)**0.5 * (x3**2+y3**2)**0.5)

def tan(cos):
    return ((1-cos)/(1+cos))**0.5

def r(x1, y1, x2, y2, x3, y3):
    tan1 = tan(cos(x1, y1, x2, y2, x3, y3))
    tan2 = tan(cos(x3, y3, x1, y1, x2, y2))
    b = ((x1-x3)**2+(y1-y3)**2)**0.5
    return b*tan1*tan2 / (tan1+tan2+2*tan1*tan2)

r1 = r(x1, y1, x2, y2, x3, y3)
r2 = r(x2, y2, x3, y3, x1, y1)
r3 = r(x3, y3, x1, y1, x2, y2)
print(max([r1, r2, r3]))