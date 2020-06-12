import sys
input = sys.stdin.readline
import heapq as hp

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

L = [[] for _ in range(N)]
for a, b in AB:
    L[a-1].append(b)

q = []
ans = 0
for n in range(N):
    for l in L[n]:
        hp.heappush(q, -l)
    p = -hp.heappop(q)
    ans += p
    print(ans)