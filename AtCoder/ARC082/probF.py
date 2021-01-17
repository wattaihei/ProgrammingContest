import sys
input = sys.stdin.buffer.readline
from bisect import bisect_right

X = int(input())
N = int(input())
A = list(map(int, input().rstrip().split()))
Q = int(input())
Query = [list(map(int, input().rstrip().split())) for _ in range(Q)]

def bet(a):
    return max(min(a, X), 0)

upper = [X]*(N+1)
lower = [0]*(N+1)
dp = [X]*(N+1) # upperになる最小のa

pre = 0
for i, a in enumerate(A):
    d = pre-a if i%2 == 0 else a-pre
    upper[i+1] = bet(upper[i]+d)
    lower[i+1] = bet(lower[i]+d)
    if i >= 1:
        dp[i+1] = dp[i] if i%2 == 0 else bet(dp[i]-(max(upper[i]+d-X, 0)))
    pre = a

for t, a in Query:
    i = bisect_right(A, t)
    d = t-A[i-1] if i > 0 else t
    if i%2 == 0:
        d = -d

    if dp[i] <= a:
        ans = upper[i]+d
    else:
        y = dp[i]-a
        ans = max(upper[i]-y, lower[i]) + d
    ans = bet(ans)
    print(ans)
