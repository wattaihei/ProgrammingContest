N = int(input())
S = [1 if a == 'o' else 0 for a in list(input())]
S.append(S[0])

def check(a0, a1):
    dp = [None]*(N+2) #TrueならSheep, FalseならWolf
    dp[0] = a0
    dp[1] = a1
    for i in range(2, N+2):
        if dp[i-2] and dp[i-1]:
            dp[i] = True if S[i-1] == 1 else False
        if dp[i-2] and not dp[i-1]:
            dp[i] = True if S[i-1] == 0 else False
        if not dp[i-2] and dp[i-1]:
            dp[i] = True if S[i-1] == 0 else False
        if not dp[i-2] and not dp[i-1]:
            dp[i] = True if S[i-1] == 1 else False
    return dp


def main():
    ok = False
    for a0 in [True, False]:
        for a1 in [True, False]:
            dp = check(a0, a1)
            if (dp[N] == a0) and (dp[N+1] == a1):
                ok = True
                break
        if ok:
            break
    if not ok:
        print(-1)
    else:
        ans = ['S' if dp[i] else 'W' for i in range(N)]
        print(''.join(ans))


if __name__ == "__main__":
    main()