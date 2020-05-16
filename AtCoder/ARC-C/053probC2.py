import sys
input = sys.stdin.readline
from operator import itemgetter

N = int(input())
Plus = []
Minus = []
for _ in range(N):
    a, b = map(int, input().split())
    if a < b:
        Plus.append((a, b, b-a))
    else:
        Minus.append((a, b, a-b))

Plus.sort(key=itemgetter(1), reverse=True)
Plus.sort(key=itemgetter(0))
Minus.sort(key=itemgetter(2))
Minus.sort(key=itemgetter(1), reverse=True)
Checks = Plus + Minus

"""
l = 0
r = 10**15
while r-l > 1:
    m = (l+r)//2
    ok = True
    now = 0
    for a, b, _ in Checks:
        if now + a > m:
            ok = False
            break
        now += a - b
    if ok:
        r = m
    else:
        l = m

print(r)
"""
ans = 0
now = 0
for a, b,_ in Checks:
    if now+a > ans:
        ans = now+a
    now += a-b
print(ans)