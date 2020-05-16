import sys
input = sys.stdin.readline
INF = 10**14

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    S = list(input().rstrip())
    Query.append((N, S))

for N, S in Query:
    dp1 = {}
    dp1[0] = {0: 0}
    ud1 = 0
    lr1 = 0
    ans = INF
    for i, s in enumerate(S):
        if s == "L":
            lr1 -= 1
        elif s == "R":
            lr1 += 1
        elif s == "U":
            ud1 += 1
        else:
            ud1 -= 1
        if lr1 in dp1 and ud1 in dp1[lr1]:
            delta = i+1-dp1[lr1][ud1]
            if delta < ans:
                ans = delta
                al = dp1[lr1][ud1]+1
                ar = i+1
        if lr1 in dp1:
            dp1[lr1][ud1] = i+1
        else:
            dp1[lr1] = {ud1: i+1}
    if ans == INF:
        print(-1)
    else:
        print(al, ar)
    