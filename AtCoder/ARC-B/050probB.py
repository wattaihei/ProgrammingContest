R, B = map(int, input().split())
x, y = map(int, input().split())

def solve():
    if R*y <= B:
        return R
    if B*x <= R:
        return B
    c1 = (R*y-B)//(x*y-1)
    c2 = (x*B-R)//(x*y-1)
    if c1 + y*(c2+1) <= B or x*(c1+1) + c2 <= R:
        return c1+c2+1
    return c1+c2

print(solve())