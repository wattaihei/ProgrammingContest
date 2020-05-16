import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for A in Query:
    A.sort()
    tmp = A[0]
    d = A[2]-A[1]
    if d > tmp:
        ans = A[0] + A[1]
    else:
        ans = A[0] + A[1] - ((tmp-d+1)//2)
    print(ans)