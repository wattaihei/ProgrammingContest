import sys
input = sys.stdin.readline


N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]

mod = 10**9+7

Last = [-1]*(M+1)
dp1 = [0]*(N+1)
dp2 = [0]*(N+1)
dp3 = [0]*(N+1)
last = -1
for i, a in enumerate(A):
    if i == 0:
        dp1[0] = 1
        dp3[0] = 1
        Last[a] = i
    else:
        last = max(Last[a], last)
        dp1[i] = (dp1[i-1] + dp2[i-1])%mod
        dp2[i] = (dp3[i-1] - dp3[last])%mod
        dp3[i] = (dp3[i-1] + dp1[i])%mod
        Last[a] = i

print((dp1[N-1]+dp2[N-1])%mod)
