import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
A = list(map(int, input().split()))

B1 = []
B2 = []
for i, a in enumerate(A):
    B1.append(a-i)
    B2.append(-a-i)

dic = {}

ans = 0
for b1, b2 in zip(B1, B2):
    if b1 in dic:
        ans += dic[b1]
    if b2 in dic:
        dic[b2] += 1
    else:
        dic[b2] = 1

print(ans)