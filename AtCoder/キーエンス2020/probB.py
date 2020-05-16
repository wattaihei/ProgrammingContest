import sys
input = sys.stdin.readline
from operator import itemgetter

N = int(input())
LR = []
for _ in range(N):
    a, b = map(int, input().split())
    LR.append((a-b, a+b))

LR.sort(key=itemgetter(1))
now_max = -10**15
ans = N
for l,r in LR:
    if l < now_max:
        ans -= 1
    else:
        now_max = r

print(ans)