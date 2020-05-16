import sys
input = sys.stdin.readline


Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for a, b, c in Query:
    ans = 0
    if a > 0:
        ans += 1
        a -= 1
    if b > 0:
        ans += 1
        b -= 1
    if c > 0:
        ans += 1
        c -= 1
    A = [a, b, c]
    A.sort()
    if A[0] >= 2:
        ans += 3
        A[0] -= 2
        A[1] -= 2
        A[2] -= 2
    elif A[0] == 1:
        if A[2] >= 2:
            A[0] -= 1
            A[1] -= 1
            A[2] -= 2
            ans += 2
        else:
            A[0] -= 1
            A[1] -= 1
            ans += 1
    else:
        if A[1] >= 1:
            A[1] -= 1
            A[2] -= 1
            ans += 1
    if min(A) > 0:
        ans += 1
    print(ans)