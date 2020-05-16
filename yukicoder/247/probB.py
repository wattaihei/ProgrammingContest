import sys
input = sys.stdin.readline

A, B = map(int, input().split())

if B == 0:
    print(1)
elif A == -1:
    print(2)
else:
    print(-1)