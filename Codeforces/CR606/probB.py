import sys
input = sys.stdin.readline
import heapq as hp

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    S = set()
    q = []
    for a in A:
        if not a in S:
            hp.heappush(q, -a)
        S.add(a)
    
    c = 0
    while q:
        a = -hp.heappop(q)
        if not a in S:
            continue
        S.remove(a)
        if a % 2 == 0:
            c += 1
            a //= 2
            hp.heappush(q, -a)
            S.add(a)
    print(c)
            
    

