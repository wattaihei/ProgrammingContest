import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
A.sort()
L = A[-1].bit_length()

canuse = [True]*N
ans = 0
for l in reversed(range(L)):
    Prob = set()
    for i, a in enumerate(A):
        if canuse[i]:
            Prob.add((a>>l)^1)
    must_add = True
    for i, a in enumerate(A):
        if canuse[i]:
            if not a>>l in Prob:
                must_add = False
                break
    if must_add:
        ans += 1<<l
    else:
        for i, a in enumerate(A):
            if canuse[i] and a>>l in Prob:
                canuse[i] = False
print(ans)