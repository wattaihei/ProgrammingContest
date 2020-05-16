import sys
input = sys.stdin.readline

Q = int(input())
Query = [int(input()) for _ in range(Q)]

for N in Query:
    if N == 1:
        print(-1)
    else:
        ans = "2" + "9"*(N-1)
        print(ans)