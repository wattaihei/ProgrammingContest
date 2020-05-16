import sys
input = sys.stdin.readline

from bisect import bisect_left, bisect_right

S = list(input().rstrip())
T = list(input().rstrip())
Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

Sa = []
Sb = []
for i, s in enumerate(S):
    if s == 'A':
        Sa.append(i)
    else:
        Sb.append(i)

Ta = []
Tb = []
for i, t in enumerate(T):
    if t == 'A':
        Ta.append(i)
    else:
        Tb.append(i)

def kind(La, Lb, l, r):
    ca = bisect_right(La, r) - bisect_left(La, l)
    cb = bisect_right(Lb, r) - bisect_left(Lb, l)
    return (ca + cb*2)%3 

for a, b, c, d in Query:
    if kind(Sa, Sb, a-1, b-1) == kind(Ta, Tb, c-1, d-1):
        print('YES')
    else:
        print('NO')