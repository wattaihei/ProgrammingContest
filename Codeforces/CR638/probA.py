import sys
input = sys.stdin.readline

Q = int(input())
Query = [int(input()) for _ in range(Q)]

for N in Query:
    ans = 2**(N//2+1) - 2
    print(ans)