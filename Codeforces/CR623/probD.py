import sys
input = sys.stdin.readline
import heapq as hp

N = int(input())
A = list(map(int, input().split()))
T = list(map(int, input().split()))
AT = {}
for a, t in zip(A, T):
    if a in AT:
        AT[a].append(t)
    else:
        AT[a] = [t]

As = sorted(list(set(A)))

q = []
S = 0
ans = 0
ind = -1
for a in As:
    while q and ind <= a:
        s = - hp.heappop(q)
        S -= s
        ans += S
        ind += 1
    
    for t in AT[a]:
        hp.heappush(q, -t)
        S += t

    #s = - hp.heappop(q)
    #S -= s

    ind = a+1

while q:
    s = - hp.heappop(q)
    S -= s
    ans += S

print(ans)