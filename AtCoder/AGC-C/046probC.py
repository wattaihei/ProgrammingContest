if __name__=='__main__':
    mod = 998244353

    import sys
    input = sys.stdin.readline

    S, K_str = input().rstrip().split()
    K = int(K_str)

    one = 0
    A = []
    for s in S:
        if s == "1":
            one += 1
        else:
            A.append(one)
            one = 0
    A.append(one)

    A = A[::-1]

    N = len(S)
    sumA = sum(A)

    dp = [[0]*(sumA+1) for _ in range(sumA+1)]
    sdp = [[0]*(sumA+1) for _ in range(sumA+1)]
    dp[0][0] = 1
    for k in range(sumA+1):
        sdp[0][k] = 1
    for a in A:
        ndp = [[0]*(sumA+1) for _ in range(sumA+1)]
        nsdp = [[0]*(sumA+1) for _ in range(sumA+1)]
        for l in range(sumA+1):
            for k in range(sumA+1):
                for j in range(1, a+1):
                    if l+j > sumA or k+j > sumA: break
                    ndp[l+j][k+j] = (ndp[l+j][k+j] + dp[l][k]) % mod
                d = sdp[l][sumA] - sdp[l][k-1] if k > 0 else sdp[l][sumA]
                ndp[l][k] = (ndp[l][k] + d) % mod
            for k in range(sumA+1):
                nsdp[l][k] = (nsdp[l][k-1] + ndp[l][k]) % mod
        dp = ndp
        sdp = nsdp

    ans = 0
    for l in range(min(sumA, K)+1):
        ans = (ans + dp[l][0]) % mod
    print(ans)