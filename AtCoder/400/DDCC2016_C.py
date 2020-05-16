import sys
input = sys.stdin.readline
import heapq as hp
INF = 10**5+2

N, X = map(int, input().split())
T = list(map(int, input().split()))
A = list(map(int, input().split()))

dic = {i:[] for i in range(INF)}
for t, a in zip(T, A):
    dic[t].append(a)

l = 0
r = INF
while r-l > 1:
    m = (r+l)//2
    #print(m)
    q = []
    score = 0
    for t in reversed(range(m+1, INF)):
        for a in dic[t]:
            hp.heappush(q, -a)
    for t in reversed(range(1, m+1)):
        for a in dic[t]:
            hp.heappush(q, -a)
        if len(q) > 0:
            s = -hp.heappop(q)
            score += s
        if score >= X:
            break
    #print(score)
    if score >= X:
        r = m
    else:
        l = m

if r == INF:
    print(-1)
else:
    print(r)