import sys
input = sys.stdin.readline

H, N = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
dp = [10**14]*(H+1)
dp[0] = 0
for a, b in AB:
    for i in range(H+1):
        if i < a:
            if dp[i] > b:
                dp[i] = b
        else:
            if dp[i] > dp[i-a]+b:
                dp[i] = dp[i-a]+b
print(dp[H])