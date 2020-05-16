import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [[0]*(N+1) for _ in range(N+1)]
B = [(a, i) for i, a in enumerate(A)]
B.sort(reverse=True)

for l, (a, i) in enumerate(B):
    length = N-l
    for left in range(l+1):
        dp[left+1][left+length] = max(dp[left+1][left+length], dp[left][left+length] + a*abs(i-left))
        dp[left][left+length-1] = max(dp[left][left+length-1], dp[left][left+length] + a*abs(left+length-1-i))
ans = 0    
for n in range(N+1):
    ans = max(ans, dp[n][n])
print(ans)