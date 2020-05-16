from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ST = [list(map(int, input().split())) for _ in range(M)]

X = [0]*(N+2)
for s, t in ST:
    X[s] += 1
    X[t+1] -= 1

P = []
s = 0
for x in range(1, N+1):
    s += X[x]
    if s == 1:
        P.append(x)

ans = []
for i, (s, t) in enumerate(ST):
    if bisect_left(P, s) == bisect_right(P, t):
        ans.append(i+1)

print(len(ans))
for a in ans:
    print(a)