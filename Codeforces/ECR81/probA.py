import sys
input = sys.stdin.readline

Q = int(input())
Query = [int(input()) for _ in range(Q)]

for N in Query:
    n = N//2
    p = N%2
    if p == 1: n -= 1
    ans = "7"*p + "1"*n
    print(ans)