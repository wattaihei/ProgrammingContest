import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N, M = map(int, input().split())
    Mat = [list(map(int, input().split())) for _ in range(N)]
    Query.append((N, M, Mat))

for N, M, Mat in Query:
    K = (N+M-1)//2
    ans = 0
    for k in range(K):
        dp1 = [0, 0]
        dp2 = [0, 0]
        for n in range(max(0, k+1-M), min(N, k+1)):
            dp1[Mat[n][k-n]] += 1
            dp2[Mat[N-1-n][M-1-(k-n)]] += 1
        ans += min(dp1[1] + dp2[1], dp1[0] + dp2[0])
    print(ans)