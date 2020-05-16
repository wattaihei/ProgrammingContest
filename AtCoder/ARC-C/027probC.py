import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
N = int(input())
TH = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(X+1) for _ in range(X+Y+1)]

for t, h in TH:
    for c in reversed(range(1, X+1)):
        for w in range(t, X+Y+1):
            a = dp[w-t][c-1]+h
            if dp[w][c] < a:
                dp[w][c] = a

ans = 0
for c in range(X+1):
    for w in range(X+Y+1):
        if dp[w][c] > ans:
            ans = dp[w][c]
print(ans)