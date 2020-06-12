import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for A, B, C, D in Query:
    if B >= A:
        print(B)
    else:
        more = A-B
        if C <= D:
            print(-1)
        else:
            print(B+(more+C-D-1)//(C-D)*C)