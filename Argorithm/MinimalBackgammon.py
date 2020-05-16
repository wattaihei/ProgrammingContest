
def main(N, T, L, B, Lose, Back):

    dp = [[0 for _ in range(T+1)] for _ in range(N+1)]
    dp[0][0] = 1


    for t in range(T):
        for n in range(N):
            if n + 6 <= N:
                for i in range(n+1, n+7):
                    if i in Lose and t+2 <= T:
                        dp[i][t+2] += dp[n][t] / 6
                    elif i in Back:
                        dp[0][t+1] += dp[n][t] / 6
                    else:
                        dp[i][t+1] += dp[n][t] / 6
            else:
                for i in range(n+1, N+1):
                    if i in Lose and t+2 <= T:
                        dp[i][t+2] += dp[n][t] / 6
                    elif i in Back:
                        dp[0][t+1] += dp[n][t] / 6
                    else:
                        dp[i][t+1] += dp[n][t] / 6
                for i in range(2*N-n-6, N):
                    if i in Lose and t+2 <= T:
                        dp[i][t+2] += dp[n][t] / 6
                    elif i in Back:
                        dp[0][t+1] += dp[n][t] / 6
                    else:
                        dp[i][t+1] += dp[n][t] / 6
        dp[-1][t+1] += dp[-1][t]

    print(dp[-1][-1])


if __name__=='__main__':
    inp = []
    while True:
        try:
            N, T, L, B = map(int, input().split()) # 横に2個
            Lose = [int(input()) for _ in range(L)]
            Back = [int(input()) for _ in range(B)]
            inp.append([N, T, L, B, Lose, Back])
        except ValueError:
            break
    for p in inp:
        main(p[0], p[1], p[2], p[3], p[4], p[5])