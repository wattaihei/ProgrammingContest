import sys
input = sys.stdin.readline
import math

N = int(input())
Query = [list(map(int, input().split())) for _ in range(N)]

def solve(a, b):
    if a == b:
        return (a-1)*2
    q = a*b-1
    s = int(math.sqrt(q))
    for n in range(s-3, s+4):
        if n*n <= q:
            t = n
    if t*t == q:
        return 2*t-1
    else:
        return 2*t-1

for a, b in Query:
    print(solve(a, b))