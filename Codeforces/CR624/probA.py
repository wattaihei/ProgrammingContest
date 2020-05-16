
import sys
input = sys.stdin.readline


Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]
for A, B in Query:
    if A == B:
        ans = 0
    elif A < B:
        if (B-A)%2 == 0:
            ans = 2
        else:
            ans = 1
    else:
        if (A-B)%2 == 0:
            ans = 1
        else:
            ans = 2
    print(ans)