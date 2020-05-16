import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for a, b in Query:
    ans = (b - a)%b
    print(ans)