import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
Ss = Counter([input().rstrip() for _ in range(N)])
m = max(Ss.values())
ans = []
for k, v in Ss.items():
    if v == m:
        ans.append(k)
ans.sort()
print(*ans, sep="\n")