import sys
input = sys.stdin.readline
from collections import deque

Q = int(input())
Query = [list(input().rstrip().split()) for _ in range(Q)]

L = deque()
for S in Query:
    if S[0] == "1":
        c, x = S[1], int(S[2])
        L.append((c, x))
    else:
        num = int(S[1])
        dic = {}
        while num > 0 and L:
            c, x = L.popleft()
            if num >= x:
                num -= x
                l = x
            else:
                l = num
                x -= num
                num = 0
                L.appendleft((c, x))
            if c in dic:
                dic[c] += l
            else:
                dic[c] = l
        ans = 0
        for v in dic.values():
            ans += v**2
        print(ans)