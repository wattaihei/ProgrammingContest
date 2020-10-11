import sys
input = sys.stdin.readline
import heapq as hp

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    KLR = [list(map(int, input().split())) for _ in range(N)]
    Query.append((N, KLR))

for N, KLR in Query:
    basic = 0
    Ls = [[] for _ in range(N)]
    Rs = [[] for _ in range(N)] 
    for k, l, r in KLR:
        if l > r:
            basic += r
            Ls[k-1].append(l-r)
        elif r > l:
            if k != N:
                basic += l
                Rs[k].append(r-l)
            else:
                basic += l
        else:
            basic += r
    
    ans = basic
    q1 = []
    for i in reversed(range(N)):
        for l in Ls[i]:
            hp.heappush(q1, -l)
        if q1:
            p = -hp.heappop(q1)
            ans += p
    
    q2 = []
    for i in range(N):
        for r in Rs[i]:
            hp.heappush(q2, -r)
        if q2:
            p = -hp.heappop(q2)
            ans += p
    
    print(ans)