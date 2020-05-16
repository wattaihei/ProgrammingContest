from bisect import bisect_right, bisect_left

N = int(input())
A = [int(input()) for _ in range(N)]

dp = [1]*N

for a in A:
    ia = bisect_right(dp, -a)
    if dp[ia] == 1:
        dp[ia] = -a
    else:
        ib = bisect_left(dp, -a+1)
        dp[ib] = -a
    #print(dp)

ans = 0
for i in range(N):
    if dp[i] != 1:
        ans += 1
print(ans)