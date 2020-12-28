import sys
input = sys.stdin.buffer.readline
from collections import deque

one = ord("1")

N = int(input())
T = list(input().rstrip())
S = list(input().rstrip())

ans = 0
wait_T = -1
wait_S = deque()
for i, (s, t) in enumerate(zip(S, T)):
    if s == one:
        wait_S.append(i)
    if t == one:
        if wait_T != -1:
            ans += i-wait_T
            wait_T = -1
        elif wait_S:
            j = wait_S.popleft()
            ans += i-j
        else:
            wait_T = i

if wait_T != -1 or wait_S:
    print(-1)
else:
    print(ans)