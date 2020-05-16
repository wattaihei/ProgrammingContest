from collections import Counter
from bisect import bisect_left

N = int(input())
A = [int(input()) for _ in range(N)]

B = list(Counter(A).keys())
B.sort()

for a in A:
    print(bisect_left(B, a))