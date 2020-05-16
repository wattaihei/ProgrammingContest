import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for A, B, C, D in Query:
    if A > B:
        A, B = B, A
    p1 = C-D
    p2 = C+D
    ans = 0
    if A <= p1 <= p2 <= B:
        ans = p1-A + B-p2
    elif A > p2 or p1 > B:
        ans = B-A
    elif p1 <= A <= p2 <= B:
        ans = B-p2
    elif A <= p1 <= B <= p2:
        ans = p1-A
    print(ans)