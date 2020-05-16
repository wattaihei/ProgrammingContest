import heapq as hp
from operator import itemgetter

N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

q = []
for i, (a, b) in enumerate(AB):
    hp.heappush(q, (a, i))

ans = 0
for _ in range(K):
    a, i = hp.heappop(q)
    ans += a
    b = AB[i][1]
    hp.heappush(q, (a+b, i))
print(ans)