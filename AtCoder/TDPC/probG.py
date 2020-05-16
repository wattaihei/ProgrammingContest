S = list(input())
N = len(S)
K = int(input())

dp = [[0]*26 for _ in range(N+1)]
dic = {}
for i in range(26):
    dic[chr(i+97)] = i

p = 0
for n in range(N-1, -1, -1):
    j = dic[S[n]]
    pre = p
    p = 0
    for i in range(26):
        if i == j:
            dp[n][i] = 1 + pre
        else:
            dp[n][i] = dp[n+1][i]
        p += dp[n][i]

ans = ''
n = 0
while n < N:
    update = False
    for i in range(26):
        if K - dp[n][i] < 0:
            update = True
            r = chr(i+97)
            ans += r
            break
        K -= dp[0][i]
    n += 1
    if not update:
        ans = 'Eel'
        break
    print(ans)
    while S[n] != r:
        n += 1
        if n >= N:
            break
    K -= 1

print(ans)