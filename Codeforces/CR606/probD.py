import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    Ss = [input().rstrip() for _ in range(N)]
    Query.append((N, Ss))

INF = 10**9

for N, Ss in Query:
    dp = [[INF, INF] for _ in range(N)]
    S0 = Ss[0]

    if S0[0] == '1' and S0[-1] == "1":
        dp[0][1] = 0
    elif S0[0] == '1' and S0[-1] == "0":
        dp[0][0] = 0
        dp[0][1] = 1
    elif S0[0] == '0' and S0[-1] == "1":
        dp[0][0] = 1
        dp[0][1] = 0
    else:
        dp[0][0] = 0
    
    for i, S in enumerate(Ss):
        if i == 0: continue
        if S[0] == '1' and S[-1] == "1":
            dp[i][1] = dp[i-1][1]
        elif S[0] == '1' and S[-1] == "0":
            dp[i][0] = dp[i-1][1]
            dp[i][1] = dp[i-1][0] + 1
        elif S[0] == '0' and S[-1] == "1":
            dp[i][0] = dp[i-1][1] + 1
            dp[i][1] = dp[i-1][0]
        else:
            dp[i][0] = dp[i-1][0]
    
    a = min(dp[N-1])
    if a >= INF:
        print(-1)
    else:
        ans = []
        for i in range(N-1):
            if min(dp[i+1]) == min(dp[i]) + 1:
                ans.append(i+1)
        print(a)
        print(" ".join([str(a) for a in ans]))
    
    