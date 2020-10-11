mod = 10**9+7

# xと最上位bitが同じでx以下のもののスコア足し上げ
def countup(x, y):
    L1 = x.bit_length()
    x -= 1<<(L1-1)
    y -= 1<<(L1-1)
    L = x.bit_length()
    dp = [[[0, 0], [0, 0]] for _ in range(L+1)]
    # 立ってるbitがlこのもの
    dp[0][0][0] = 1
    for i in range(L):
        a = x&(1<<(L-1-i))
        b = y&(1<<(L-1-i))
        if a:
            if b:
                dp[i+1][0][0] = dp[i][0][0]
                dp[i+1][0][1] = 2*dp[i][0][1] % mod
                dp[i+1][1][0] = dp[i][1][0]
                dp[i+1][1][1] = (3*dp[i][1][1] + dp[i][0][1]) % mod
            else:
                dp[i+1][0][0] = dp[i][0][0]
                dp[i+1][0][1] = (dp[i][0][0] + 2*dp[i][0][1]) % mod
                dp[i+1][1][0] = (dp[i][0][0] + 2*dp[i][1][0]) % mod
                dp[i+1][1][1] = (3*dp[i][1][1] + dp[i][0][1] + dp[i][1][0]) % mod 
        else:
            if not b:
                dp[i+1][0][0] = dp[i][0][0]
                dp[i+1][0][1] = dp[i][0][1]
                dp[i+1][1][0] = 2*dp[i][1][0] % mod
                dp[i+1][1][1] = (3*dp[i][1][1] + dp[i][1][0]) % mod
            else:
                dp[i+1][0][1] = dp[i][0][1]
                dp[i+1][1][0] = dp[i][1][0]
                dp[i+1][1][1] = 3*dp[i][1][1] % mod
    return sum(dp[L][0]) + sum(dp[L][1]) % mod


def main():
    Left, Right = map(int, input().split())
    ans = 0
    while True:
        # print(bin(Right))
        bl = Left.bit_length()
        br = Right.bit_length()
        if bl == br:
            ans = (ans + countup(Right, Left)) % mod
            break
        else:
            ans = (ans + countup(Right, (1<<(br-1)))) % mod
            Right = (1<<(br-1))-1
    
    print(ans)

if __name__ == "__main__":
    main()