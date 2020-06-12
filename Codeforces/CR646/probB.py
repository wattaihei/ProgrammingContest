import sys
input = sys.stdin.readline

Q = int(input())
Ss = [list(input().rstrip()) for _ in range(Q)]

for S in Ss:
    L = len(S)
    dp = [[0, 0] for _ in range(L+1)]
    fla = 0
    for i in range(L):
        if S[i] == "0":
            dp[i+1][0] = dp[i][0] + 1
            dp[i+1][1] = dp[i][1]
        else:
            dp[i+1][0] = dp[i][0] 
            dp[i+1][1] = dp[i][1] + 1
        if i < L-1 and S[i] != S[i+1]:
            fla += 1
    if fla < 2:
        ans = 0
    else:
        ans = min(dp[L][0], dp[L][1])
        for i in range(L-1):
            if S[i] == "0" and S[i+1] == "1":
                ans = min(ans, dp[i+1][1]+ (dp[L][0]-dp[i+2][0]))
            elif S[i] == "1" and S[i+1] == "0":
                ans = min(ans, dp[i+1][0] + (dp[L][1]-dp[i+2][1]))

    print(ans)