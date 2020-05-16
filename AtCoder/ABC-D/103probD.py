import heapq

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

Bri = [[] for _ in range(N+1)]
for a, b in AB:
    Bri[a].append(b)

q = []
ans = 0
for j in range(1, N+1):
    if q:
        if q[0] == j:
            q = []
            ans += 1
    for p in Bri[j]:
        heapq.heappush(q, p)
print(ans)