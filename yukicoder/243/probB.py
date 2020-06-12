import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
A = list(map(int, input().split()))
S = input().rstrip()

q = deque()
for a in A:
    q.append(a)


for s in S:
    if s == "L":
        q.append(0)
        a = q.popleft()
        b = q.popleft()
        q.appendleft(a+b)
    else:
        q.appendleft(0)
        a = q.pop()
        b = q.pop()
        q.append(a+b)

print(*q)