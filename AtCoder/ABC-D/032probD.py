import sys
input = sys.stdin.readline
from bisect import bisect_right

N, W = map(int, input().split())
Vs = [None]*N
Ws = [None]*N
for i in range(N):
    v, w = map(int, input().split())
    Vs[i] = v
    Ws[i] = w

if max(Ws) <= 1000:
    dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
    for n in range(N):
        for w in range(W+1):
            if Ws[n] > w:
                dp[n+1][w] = dp[n][w]
            else:
                dp[n+1][w] = max(dp[n][w], dp[n][w-Ws[n]]+Vs[n])
    print(dp[N][W])
elif max(Vs) <= 1000:
    INF = 10**16
    V = sum(Vs)
    dp = [[INF for _ in range(V+1)] for _ in range(N+1)]
    dp[0][0] = 0
    for n in range(N):
        for v in range(V+1):
            if Vs[n] > v:
                dp[n+1][v] = dp[n][v]
            else:
                dp[n+1][v] = min(dp[n][v], dp[n][v-Vs[n]]+Ws[n])
    ans = 0
    for v in range(V+1):
        if dp[N][v] <= W:
            ans = v
    print(ans)
else:
    V1 = Vs[:(N//2)]; V2 = Vs[(N//2):]
    W1 = Ws[:(N//2)]; W2 = Ws[(N//2):]
    L1 = N//2; L2 = N - N//2

    WV = []
    for bit in range(1<<L1):
        w = 0; v = 0
        for i in range(L1):
            if (1<<i)&bit:
                w += W1[i]; v += V1[i]
        WV.append((w, v))
    WV.sort()
    maxV = [0]
    maxW = [0]
    for x, v in WV:
        maxV.append(max(maxV[-1], v))
        maxW.append(x)
    
    ans = 0
    for bit in range(1<<L2):
        w = 0; v = 0
        for i in range(L2):
            if (1<<i)&bit:
                w += W2[i]; v += V2[i]
        bi = bisect_right(maxW, W-w)
        if bi == 0: continue
        ans = max(ans, maxV[bi-1]+v)
    print(ans)