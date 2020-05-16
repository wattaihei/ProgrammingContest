import sys
input = sys.stdin.readline
import heapq as hp

N = int(input())
A = list(map(int, input().split()))

q = []
ans = []
for a in A:
    ans.append(len(q))
    while q:
        b = hp.heappop(q)
        if b > a:
            hp.heappush(q, b)
            break
    hp.heappush(q, a)

print(*ans, sep="\n")