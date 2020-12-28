import sys
input = sys.stdin.buffer.readline
from math import gcd

N = int(input())
A = list(map(int, input().split()))

ans = A[0]
for a in A:
    ans = gcd(ans, a)
print(ans)

