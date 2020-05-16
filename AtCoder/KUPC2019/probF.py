from operator import itemgetter
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
LRB = [list(map(int, input().split())) for _ in range(M)]

B = []
for i, a in enumerate(A):
    B.append((i, a))

B.sort(key=itemgetter(1))

ans = 0
used = [False for _ in range(M)]
for i, b in B:
    canuse = 0
    for j, (l, r, s) in enumerate(LRB):
        if not used[j] and l-1 <= i <= r-1:
            used[j] = True
            canuse += s
    ans += max(0, canuse-b)

print(ans)