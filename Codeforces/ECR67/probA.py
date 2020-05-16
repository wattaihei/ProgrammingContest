Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for n, s, t in Query:
    ans = max(n-s+1, n-t+1)
    print(ans)