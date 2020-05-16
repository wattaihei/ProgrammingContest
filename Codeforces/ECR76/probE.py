import sys
input = sys.stdin.readline


K1, K2, K3 = map(int, input().split())
N = K1 + K2 + K3
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

state = []
P = []
ind = 0
for b in B:
    while ind < K3 and C[ind] < b:
        state.append(1)
        P.append(C[ind])
        ind += 1
    state.append(0)
    P.append(b)

while ind < K3:
    state.append(1)
    P.append(C[ind])
    ind += 1


dp = [[0, 0] for _ in range(K2+K3+1)]

for i in reversed(range(K2+K3)):
    if state[i] == 0:
        dp[i][0] = min(dp[i+1][0], dp[i+1][1])
        dp[i][1] = dp[i+1][1] + 1
    else:
        dp[i][0] = min(dp[i+1][0], dp[i+1][1]) + 1
        dp[i][1] = dp[i+1][1]

ans = 10**14
indp = 0
inda = 0
for n in range(N+1):
    while indp < K3+K2 and P[indp] <= n:
        indp += 1
    while inda < K1 and A[inda] <= n:
        inda += 1
    ans = min(ans, indp + (K1 - inda) + min(dp[indp]))

print(ans)