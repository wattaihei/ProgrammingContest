import sys
input = sys.stdin.readline

Q = int(input())
Query = [int(input()) for _ in range(Q)]

for n in Query:
    if n == 2:
        ans = 2
    elif n % 2 == 1:
        ans = 1
    else:
        ans = 0
    print(ans)