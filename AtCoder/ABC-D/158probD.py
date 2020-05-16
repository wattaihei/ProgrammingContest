import sys
input = sys.stdin.readline

from collections import deque


S = list(input().rstrip())
Q = int(input())
Query = [list(map(str, input().split())) for _ in range(Q)]

q = deque()
gyaku = False
for s in S:
    q.append(s)

for A in Query:
    if A[0] == "1":
        gyaku =  not gyaku
    else:
        if (gyaku and A[1] == "1") or (not gyaku and A[1] == "2"):
            q.append(A[2])
        else:
            q.appendleft(A[2])


S = []
for p in q:
    S.append(p)

if gyaku:
    S = S[::-1]

print("".join(S))