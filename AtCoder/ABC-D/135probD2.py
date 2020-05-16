
def main():
    S = list(input())

    dp = [[0 for _ in range(13)] for _ in range(len(S))]
    # 上からj桁目までの数を13で割ったあまりがiであるものの個数

    for i, sk in enumerate(S):
        if i == 0:
            if sk == '?':
                for j in range(10):
                    dp[0][j] = 1
            else:
                s = int(sk)
                dp[0][s] = 1
            continue
        if sk == '?':
            for j in range(13):
                for l in range(10): # 上からi桁目に入れる数字
                    k = (10*j+l)%13
                    dp[i][k] += dp[i-1][j]
        else:
            s = int(sk)
            for j in range(13):
                k = (10*j+s)%13
                dp[i][k] += dp[i-1][j]
        for j in range(13):
            dp[i][j] = dp[i][j] % 1000000007

    print(dp[-1][5])

if __name__ == '__main__':
    main()