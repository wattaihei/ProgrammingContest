import sys
input = sys.stdin.readline
import heapq as hp

X, Y, A, B, C = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))

q1 = []
S1 = 0
for p in P:
    hp.heappush(q1, p)
    S1 += p

while len(q1) > X:
    p = hp.heappop(q1)
    S1 -= p

q2 = []
S2 = 0
for q in Q:
    hp.heappush(q2, q)
    S2 += q

while len(q2) > Y:
    p = hp.heappop(q2)
    S2 -= p


tmp = S1 + S2
ans = S1 + S2
R.sort(reverse=True)
for r in R:
    p1 = hp.heappop(q1)
    p2 = hp.heappop(q2)
    if p1 <= p2:
        if r >= p1:
            tmp += r - p1
            ans = max(ans, tmp)
            hp.heappush(q1, r)
            hp.heappush(q2, p2)
        else:
            break
    else:
        if r >= p2:
            tmp += r - p2
            ans = max(ans, tmp)
            hp.heappush(q1, p1)
            hp.heappush(q2, r)
        else:
            break

print(ans)