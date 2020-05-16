import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

P = []
p = 0
for a in A:
    if a > 0:
        p += a
    P.append(p)

S = [0]
s = 0
for a in A:
    s += a
    S.append(s)

ans = 0
for i in range(N-K+1):
    others = 0
    if i != 0:
        others += P[i-1]
    others += P[-1] - P[i+K-1]
    ans = max(ans, others)
    ans = max(ans, others+(S[i+K]-S[i]))

print(ans)