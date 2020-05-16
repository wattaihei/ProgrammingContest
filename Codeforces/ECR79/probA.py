import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]
for A in Query:
    A.sort()
    if A[2] > A[1] + A[0] + 1:
        print("No")
    else:
        print("Yes")