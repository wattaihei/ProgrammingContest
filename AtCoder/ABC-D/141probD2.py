import heapq as hp
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

q = []
for a in A:
    hp.heappush(q, -a)

for i in range(M):
    #print(q)
    b = hp.heappop(q)

    c = b//2
    if b % 2 != 0:
        c += 1
    hp.heappush(q, c)

ans = 0
for a in q:
    ans += -a
print(ans)