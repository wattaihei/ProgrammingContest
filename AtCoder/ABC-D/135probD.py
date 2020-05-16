S = list(input())

S = S[::-1]

dp = [[0 for _ in range(10)] for _ in range(len(S))]
if S[0] == '?':
    for i in range(10):
        dp[0][i] = 1
else:
    dp[0][int(S[0])] = 1

for i, s in enumerate(S):
    if s == '?':
        for d in range(10):
            for a in range(10):
                k = 13*a+dp[i][a]
                dp[i+1][(k//10)%100] += dp[i][a]
                dp[i+2][k//100] += dp[i][a]
            continue
    si = int(s)
    k = 13*si+dp[i][si]
    dp[i+1][(k//10)%100] += dp[i][si]
    dp[i+2][k//100] += dp[i][si]
    print(dp)
            