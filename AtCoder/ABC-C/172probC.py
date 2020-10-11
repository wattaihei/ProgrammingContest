import sys
input = sys.stdin.readline

from bisect import bisect_right

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

AA = [0]
for a in A:
    AA.append(AA[-1]+a)
BB = [0]
for b in B:
    BB.append(BB[-1]+b)

ans = 0
for i, aa in enumerate(AA):
    if aa > K: break
    ind = bisect_right(BB, K-aa)-1
    ans = max(ans, ind+i)

print(ans)