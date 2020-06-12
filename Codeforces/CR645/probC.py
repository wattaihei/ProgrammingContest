import sys
input = sys.stdin.readline


Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for x1, y1, x2, y2 in Query:
    a = x2-x1; b= y2-y1
    ans = a*b+1
    print(ans)