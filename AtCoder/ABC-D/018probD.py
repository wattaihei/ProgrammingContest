import sys
input = sys.stdin.readline
from itertools import combinations

N, M, P, Q, R = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(R):
    a, b, c = map(int, input().split())
    graph[a-1].append((b-1, c))

ans = 0
for Com in combinations(range(N), P):
    Scores = [0]*M
    for p in Com:
        for man, v in graph[p]:
            Scores[man] += v
    Scores.sort(reverse=True)
    ans = max(ans, sum(Scores[:Q]))
print(ans)