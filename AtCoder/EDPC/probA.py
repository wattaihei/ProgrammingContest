import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int, input().split()))

dp = [None]*N
dp[0] = 0
dp[1] = abs(H[0]-H[1])

for i in range(2, N):
    dp[i] = min(dp[i-2]+abs(H[i]-H[i-2]), dp[i-1]+abs(H[i]-H[i-1]))

print(dp[-1])