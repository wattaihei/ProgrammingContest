import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
RH = [list(map(int, input().split())) for _ in range(N)]

Dic = {}
for R, H in RH:
    if not R in Dic:
        Dic[R] = [0, 0, 0]
        Dic[R][H-1] += 1
    else:
        Dic[R][H-1] += 1

S = sorted(list(Dic.keys()))
P = []
p = 0
for s in S:
    p += sum(Dic[s])
    P.append(p)

for R, H in RH:
    ind = bisect_left(S, R)
    win = P[ind-1] if ind > 0 else 0
    lose = P[-1] - P[ind]
    mid = 0
    H -= 1
    mid += Dic[R][H] - 1
    lose += Dic[R][H-1]
    win += Dic[R][H-2]

    print(win, lose, mid)