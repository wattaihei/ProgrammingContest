import sys
input = sys.stdin.readline

INF = 10**15

N, M = map(int, input().split())
A = []
for _ in range(M):
    S, strC = input().split()
    bit = 0
    for i in range(N):
        if S[N-i-1] == "Y":
            bit += (1<<i)
    A.append((bit, int(strC)))

dp = [INF]*(1<<N)
dp[0] = 0
for bit, C in A:
    dp2 = dp[:]
    for nbit in range(1<<N):
        dp2[nbit|bit] = min(dp2[nbit|bit], dp[nbit]+C)
    dp = dp2

a = dp[(1<<N)-1]
if a == INF:
    print(-1)
else:
    print(a)