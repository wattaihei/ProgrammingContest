import sys
import heapq
input = sys.stdin.readline
N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

P = {}
for a, b in AB:
    if a <= M:
        if not a in P.keys():
            P[a] = [b]
        else:
            P[a].append(b)

B = sorted(P.items(), key=lambda x:x[0], reverse=True)
Q = []
for k, v in B:
    v.sort(reverse=True)
    A = v[:M-k+1]
    for a in A:
        heapq.heappush(Q, a)
    maxp = max(len(Q)-M+k-1, 0)
    for _ in range(maxp):
        heapq.heappop(Q)

print(sum(Q))