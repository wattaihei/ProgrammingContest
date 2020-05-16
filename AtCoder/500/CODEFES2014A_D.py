from itertools import combinations

N, K = map(int, input().split())
S = str(N)
L = len(S)

ans = 10**18
NUMs = combinations(range(10), K)
for NUM in NUMs:
    # 超える中で一番小さい
    s = str(NUM[0])
    if NUM[0] == 0:
        if len(NUM) == 1:
            continue
        else:
            s = str(NUM[1])
    dp = ["", s]
    for l in range(L):
        n = int(S[l])
        minnum = 10
        exceednum = 10
        exists = False
        for num in NUM:
            minnum = min(minnum, num)
            if num == n:
                exists = True
            elif num > n:
                exceednum = min(exceednum, num)
        if dp[0] != "a":
            if exists:
                dp[0] += str(n)
                dp[1] += str(minnum)
            else:
                if exceednum != 10:
                    dp[1] = dp[0] + str(exceednum)
                else:
                    dp[1] += str(minnum)
                dp[0] = "a"
        else:
            dp[1] += str(minnum)
    ans = min(ans, int(dp[1]) - N)
    if dp[0] != "a":
        ans = 0

    # 下回る中で一番大きい
    dp = ["", ""]
    for l in range(L):
        n = int(S[l])
        maxnum = -1
        belownum = -1
        exists = False
        for num in NUM:
            maxnum = max(maxnum, num)
            if num == n:
                exists = True
            elif num < n:
                belownum = max(belownum, num)
        if l == 0:
            if exists:
                dp[0] += str(n)
            else:
                dp[0] = "a"
            if belownum != -1:
                dp[1] += str(belownum)
        else:
            if dp[0] != "a":
                if exists:
                    dp[0] += str(n)
                    dp[1] += str(maxnum)
                else:
                    if belownum != -1:
                        dp[1] = dp[0] + str(belownum)
                    else:
                        dp[1] += str(maxnum)
                    dp[0] = "a"
            else:
                dp[1] += str(maxnum)
    
    if dp[1] == "":
        dp[1] = "0"
    ans = min(ans, N-int(dp[1]))
    if dp[0] != "a":
        ans = 0

print(ans)