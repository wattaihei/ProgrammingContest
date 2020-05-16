N, mW = map(int, input().split())
W = []
V = []
for i in range(N):
    w, v = map(int, input().split())
    if i == 0:
        w0 = w
        W.append(0)
    else:
        W.append(w-W[0])
    V.append(v)

dp = [[[0]*(4*N) for _ in range(N)] for _ in range(N+1)]
arrangedV = sorted(V, reverse=True)

for k in range(N+1):
    Wk = mW - w0*k
    if Wk < 0:
        break
    else:
        for i in range(N):
            for j in range(Wk):
                if i == 0:
                    dp[k][i][j] = 0
                elif j < W[i] or k == 0:
                    dp[k][i][j] = dp[k][i-1][j]
                else:
                    dp[k][i][j] = max(dp[k][i-1][j], dp[k-1][i-1][j-W[i]] + V[i])
for l in dp:
    print(l)