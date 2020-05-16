import sys
input = sys.stdin.readline

W = int(input())
N, K = map(int, input().split())
AB = []
for _ in range(N):
    a, b = map(int, input().split())
    AB.append((a, b))
    
dp = [0 for _ in range((W+1)*(K+1))]

for i in range(N):
    a, b = AB[i]
    dp_n = [0 for _ in range((W+1)*(K+1))]
    for k in range(K):
        for w in range(W+1):
            if w-a >= 0:
                dp_n[(k+1)*(W+1)+w] = max(dp[(k+1)*(W+1)+w], dp[k*(W+1)+w-a]+b)
            else:
                dp_n[(k+1)*(W+1)+w] = dp[(k+1)*(W+1)+w]
    dp = dp_n
ans = dp[K*(W+1)+W]
print(ans)
