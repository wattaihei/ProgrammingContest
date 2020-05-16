import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for h, m in Query:
    ans = (23-h)*60 + (60-m)
    print(ans)