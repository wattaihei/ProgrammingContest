A, B = map(str, input().split())

def count(N):
    L = len(N)
    dp = [[[0, 0], [0, 0]] for _ in range(L+1)]
    dp[0][0][0] = 1
    for l in range(L):
        a = int(N[l])
        for isless in [0, 1]:
            for ok in [0, 1]:
                for num in range(10):
                    if num < a:
                        if num in [4, 9]:
                            dp[l+1][1][1] += dp[l][ok][isless]
                        else:
                            dp[l+1][ok][1] += dp[l][ok][isless]
                    elif a == num or isless:
                        if num in [4, 9]:
                            dp[l+1][1][isless] += dp[l][ok][isless]
                        else:
                            dp[l+1][ok][isless] += dp[l][ok][isless]
    return dp[L][1][0] + dp[L][1][1] - 1

a1 = count(str(int(A)-1))
a2 = count(B)
print(a2 - a1)