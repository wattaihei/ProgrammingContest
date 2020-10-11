import sys
input = sys.stdin.buffer.readline

Q = int(input())
for _ in range(Q):
    N = int(input())
    S = list(input().rstrip())

    dp = [[0]*26 for _ in range(N+1)]
    for i, s in enumerate(S):
        dp[i+1] = dp[i][:]
        dp[i+1][s-ord("a")] += 1

    K = N.bit_length()-1
    ans = N
    s = 0
    for bit in range(N):
        score = N
        left = 0
        right = N
        for i in range(K):
            leng = 2**(K-i-1)
            if bit&(1<<i):
                score -= dp[left+leng][s+i] - dp[left][s+i]
                left += leng
            else:
                score -= dp[right][s+i] - dp[right-leng][s+i]
                right -= leng
        if S[left] - ord("a") == s + K:
            score -= 1
        if score < ans:
            ans = score
    print(ans)