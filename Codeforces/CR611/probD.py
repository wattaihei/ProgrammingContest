import sys
input = sys.stdin.readline

import heapq as hp

N, M = map(int, input().split())
A = list(map(int, input().split()))
checked = set(A)
q = []
for a in A:
    xs = [a+1, a-1]
    for x in xs:
        if not x in checked:
            hp.heappush(q, (1, x))
            checked.add(x)

S = 0
ans = []
for _ in range(M):
    s, ind = hp.heappop(q)
    S += s
    ans.append(ind)
    xs = [ind+1, ind-1]
    for x in xs:
        if not x in checked:
            hp.heappush(q, (s+1, x))
            checked.add(x)

print(S)
print(*ans)