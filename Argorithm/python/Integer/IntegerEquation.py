# (x0, y0, gcd) of ax + by = gcd(a, b)
def extGCD(a, b):
    if b == 0:
        return 1, 0, a
    x, y, g = extGCD(b, a%b)
    return y, x-(a//b)*y, g

# (x, y) of ax + by = c
# if do not have solution return False
# if all (x, y) is solution return True
# else (x, y) can be described as:
# x = x0 + x1 * l
# y = y0 + y1 * l 
# returns (x0, x1, y0, y1)
def integerEquation(a, b, c):
    if a == 0 and b == 0: return c == 0
    x0, y0, g = extGCD(a, b)
    if c%g != 0: return False
    d = c//g
    return (d*x0, b//g, d*y0, -(a//g))

def euler_phi(n):
    primes = []
    tmp = n
    for a in range(2, int(sqrt(n))+3):
        if tmp%a == 0:
            primes.append(a)
            while tmp%a == 0:
                tmp //= a
    if tmp > 1: primes.append(tmp)
    ret = n
    for p in primes:
        ret = ret * (p-1) // p
    return ret

# from math import gcd
# def check(inp):
#     a, b, c = inp
#     print(inp, end=" ")
#     outp = integerEquation(a, b, c)
#     print(outp)
#     if a == b == 0:
#         if c == 0: return outp == True
#         return outp == False
#     if c%gcd(a,b) != 0: return outp == False
#     x0, x1, y0, y1 = outp
#     ok = True
#     for l in range(-10, 10):
#         x = x0 + x1*l
#         y = y0 + y1*l
#         if a*x + b*y != c: ok = False
#     return ok

# from random import randint

# while True:
#     inp = [randint(-100, 100) for _ in range(3)]
#     res = check(inp)
#     if not res:
#         print("wrong answer")
#         break