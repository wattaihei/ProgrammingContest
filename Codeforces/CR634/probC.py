import sys
input = sys.stdin.readline
from collections import Counter

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    C = Counter(A)
    B = max(list(C.values()))
    ans = max(min(len(C)-1, B), min(len(C), B-1))
    print(ans)