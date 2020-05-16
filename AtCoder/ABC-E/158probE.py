import sys
input = sys.stdin.readline
from collections import Counter

N, mod = map(int, input().split())
S = list(input().rstrip())

if mod == 2 or mod == 5:
    ans = 0
    for i, s in enumerate(S):
        if int(s)%mod==0:
            ans += i+1
else:
    dp = [0]
    t = 1
    for s in reversed(S):
        dp.append((dp[-1]+int(s)*t)%mod)
        t = t*10%mod

    ans = 0
    C = Counter(dp)
    for v in C.values():
        ans += v*(v-1)//2

print(ans)