import sys
input = sys.stdin.readline

import heapq as hp

N, K, D = map(int, input().split())
A = list(map(int, input().split()))

T = [[] for _ in range(N)]
for i, a in enumerate(A):
    t = max(K-(N-i+D-1)//D, 0)
    T[t].append((a, i))

q = []
ans = []
maxind = -10**14
for k in range(K):
    for a, ind in T[k]:
        hp.heappush(q, (a, ind))
    
    if not q:
        ans = []
        break
    while q:
        a, ind = hp.heappop(q)
        if ind < maxind: continue
        ans.append(a)
        maxind = max(maxind, ind+D)
        break

if not ans:
    print(-1)
else:
    print(*ans)