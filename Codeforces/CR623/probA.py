import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for a, b, x, y in Query:
    A = [a*(b-y-1), a*y, x*b, (a-x-1)*b]
    print(max(A))