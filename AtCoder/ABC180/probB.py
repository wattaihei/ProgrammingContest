import sys
input = sys.stdin.buffer.readline
import math

N = int(input())
A = list(map(int, input().split()))

a = 0
b = 0
c = 0
for x in A:
    a += abs(x)
    b += x**2
    c = max(c, abs(x))

print(a)
print(math.sqrt(b))
print(c)