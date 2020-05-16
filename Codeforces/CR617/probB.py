import sys
input = sys.stdin.readline

Q = int(input())
Query = [int(input()) for _ in range(Q)]

for N in Query:
    ans = 0
    while N >= 10:
        a, b = N//10, N%10
        ans += a*10
        N = b+a
    ans += N
    print(ans)