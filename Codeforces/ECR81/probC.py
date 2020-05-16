import sys
input = sys.stdin.readline
from bisect import bisect_right

Q = int(input())
Query = []
for _ in range(Q):
    S = list(input().rstrip())
    T = list(input().rstrip())
    Query.append((S, T))

for S, T in Query:
    L = len(T)
    dic = {}
    for i, s in enumerate(S):
        if not s in dic:
            dic[s] = [i]
        else:
            dic[s].append(i)
    ans = 1
    ind = -1
    for t in T:
        if not t in dic:
            ans = -1
            break
        p = bisect_right(dic[t], ind)
        if p == len(dic[t]):
            ans += 1
            ind = dic[t][0]
        else:
            ind = dic[t][p]
    print(ans)
