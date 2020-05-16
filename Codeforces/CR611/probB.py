import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for n, k in Query:
    m = n%k
    if 0 <= m <= k//2:
        ans = n
    else:
        ans = n//k*k+k//2
    print(ans)