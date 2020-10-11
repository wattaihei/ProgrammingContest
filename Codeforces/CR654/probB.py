import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for N, R in Query:
    a = min(R, N-1)
    ans = a*(a+1)//2
    if R >= N: ans += 1
    print(ans)