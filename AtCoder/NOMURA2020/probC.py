import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

ans = 0
tmp_max = 1
dp = [0]*(N+1)
for i, a in enumerate(A):
    if a <= tmp_max:
        dp[i] = tmp_max
        tmp_max = 2*(tmp_max-a)
    else:
        ans = -1
        break
if ans == -1:
    print(ans)
else:
    tmp = 0
    for i in reversed(range(N+1)):
        if tmp + A[i] >= dp[i]:
            ans += dp[i]
            tmp = dp[i]
        else:
            ans += tmp + A[i]
            tmp += A[i]
    print(ans)