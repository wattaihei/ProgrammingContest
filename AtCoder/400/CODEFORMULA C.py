import sys
input = sys.stdin.buffer.readline
import heapq as hp

N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

defined = set()
q = []
for i, B in enumerate(A):
    for j, b in enumerate(B):
        hp.heappush(q, (i+N*j, b))
    remainG = N-1-i
    for_ret = []
    while q:
        seq, idx = q[0]
        if idx in defined:
            hp.heappop(q)
            continue
        if len(defined) + remainG*(seq//N) < K:
            for_ret.append(idx)
            defined.add(idx)
        else:
            break
    for_ret.sort()
    print(" ".join(map(str,for_ret)))