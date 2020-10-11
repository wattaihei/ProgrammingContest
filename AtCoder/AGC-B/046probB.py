import sys
input = sys.stdin.readline

mod = 998244353


NN = 10**4 # 使うデータによって変える

inv = [0]
for i in range(1, NN):
    inv.append(pow(i, mod-2, mod))

def main():
    A, B, C, D = map(int, input().split())
    dp = [[0]*(D+1) for _ in range(C+1)]
    dp2 = [[0]*(D+1) for _ in range(C+1)]


    for w in range(B-1, D+1):
        dp[A][w] = 0
        dp2[A][w] = pow(A, (D-B), mod)


    for c in range(A+1, C+1):
        if D - B - 1 >= 0:
            t = pow(c*inv[c-1] % mod, D-B-1, mod)
        kakeru = (c-1)*inv[c] % mod
        dp[c][B] = pow(B,c-A,mod) * pow(c, D-B, mod) % mod
        dp2[c][B] = dp[c][B]
        for d in range(B+1, D+1):
            dp[c][d] = (dp2[c-1][d-1] + dp[c-1][d]*d % mod ) * t % mod
            t = t * kakeru % mod
            dp2[c][d] = (dp2[c][d-1] + dp[c][d]) % mod

    print(dp2[C][D])


if __name__ == "__main__":
    main()