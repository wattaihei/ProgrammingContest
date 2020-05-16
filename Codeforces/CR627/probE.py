import sys
input = sys.stdin.readline

N, H, L, R = map(int, input().split())
A = list(map(int, input().split()))

dp = [0]*(N+1)

B = [0]
for a in A:
    B.append((B[-1]+a)%H)
#print(B)
for i in range(N):
    start = B[i+1]
    ndp = [0]*(N+1)
    ndp[0] = dp[0]
    for p in range(i+1):
        ndp[p+1] = max(dp[p], dp[p+1])
        nows = (start - p)%H
        if L <= nows <= R:
            ndp[p] = max(dp[p] + 1, ndp[p])
        nows2 = (start - p - 1)%H
        if L <= nows2 <= R:
            ndp[p+1] = max(dp[p] + 1, ndp[p+1])       
    dp = ndp
    #print(dp)

print(max(dp))