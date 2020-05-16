from bisect import bisect_left
import sys
input = sys.stdin.readline

W, H = map(int, input().split())
P = [int(input()) for _ in range(W)]
Q = [int(input()) for _ in range(H)]

P.sort()
Q.sort(reverse=True)

sP = [0]
a = 0
for p in P:
    a += p
    sP.append(a)

ans = sP[-1]
for q in Q:
    ip = bisect_left(P, q)
    ans += q*(W+1-ip) + sP[ip]
print(ans)