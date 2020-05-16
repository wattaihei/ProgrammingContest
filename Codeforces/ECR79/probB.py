import sys
input = sys.stdin.readline
from bisect import bisect_right

Q = int(input())
Query = []
for _ in range(Q):
    N, S = map(int, input().split())
    A = list(map(int, input().split()))
    Query.append((N, S, A))

for N, S, A in Query:
    B = [0]
    for i, a in enumerate(A):
        B.append(B[-1]+a)

    if B[-1] <= S:
        ans = 0
    else:
        num = -1
        max_p = -1
        for i, a in enumerate(A):
            if a > max_p:
                max_p = a
                ind = i+1
            if B[i+1] - max_p <= S:
                if i > num:
                    num = i
                    ans = ind
        
    print(ans)
    