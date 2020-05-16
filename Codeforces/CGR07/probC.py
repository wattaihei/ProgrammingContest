import sys
input = sys.stdin.readline
mod = 998244353


N, K = map(int, input().split())
A = list(map(int, input().split()))

P = []
ans1 = 0
for i, a in enumerate(A):
    if a >= N-K+1:
        ans1 += a
        P.append(i)

ans2 = 1
for i in range(len(P)-1):
    d = P[i+1] - P[i]
    ans2 = ans2 * d % mod

print(ans1, ans2)